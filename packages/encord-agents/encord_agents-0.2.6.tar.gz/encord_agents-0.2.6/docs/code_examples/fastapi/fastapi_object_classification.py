# 1. Import dependencies, authenticate with Encord, and set up the Project.
import os

from anthropic import Anthropic
from encord.objects.ontology_labels_impl import LabelRowV2
from fastapi import Depends
from typing_extensions import Annotated

from encord_agents.core.data_model import InstanceCrop
from encord_agents.core.ontology import OntologyDataModel
from encord_agents.core.utils import get_user_client
from encord_agents.fastapi.cors import get_encord_app
from encord_agents.fastapi.dependencies import (
    FrameData,
    dep_label_row,
    dep_object_crops,
)

# Initialize FastAPI app
app = get_encord_app()

# User client and ontology setup
client = get_user_client()
# Ensure you insert your Project's unique identifier.
project = client.get_project("<project_id>")
generic_ont_obj, *other_objects = sorted(
    project.ontology_structure.objects,
    key=lambda o: o.title.lower() == "generic",
    reverse=True,
)

# 2. Create a data model and a system prompt based on the Project Ontology to tell Claude how to structure its response.
data_model = OntologyDataModel(other_objects)
system_prompt = f"""
You're a helpful assistant that's supposed to help fill in 
json objects according to this schema:

`{data_model.model_json_schema_str}`

Please only respond with valid json.
"""

# 3. Set up an Anthropic API client to establish communication with the Claude model.
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
anthropic_client = Anthropic(api_key=ANTHROPIC_API_KEY)


# 4. Define the Editor Agent.
@app.post("/object_classification")
async def classify_objects(
    frame_data: FrameData,
    lr: Annotated[LabelRowV2, Depends(dep_label_row)],
    crops: Annotated[
        list[InstanceCrop],
        Depends(dep_object_crops(filter_ontology_objects=[generic_ont_obj])),
    ],
):
    """Classify generic objects using Claude."""
    changes = False
    # Iterating through each object crop.
    for crop in crops:
        # 5. Call Claude with Image Crops.
        # Sending each crop image to Claude for analysis.
        message = anthropic_client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1024,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": [crop.b64_encoding(output_format="anthropic")],
                }
            ],
        )

        # 6. Parse Claude's Response and Update Labels.
        try:
            # Parsing Claude's response into an updated object instance.
            instance = data_model(message.content[0].text)

            coordinates = crop.instance.get_annotation(frame=frame_data.frame).coordinates
            instance.set_for_frames(
                coordinates=coordinates,
                frames=frame_data.frame,
                confidence=0.5,
                manual_annotation=False,
            )
            # Updating the label row by removing the original object and adding the newly classified instance.
            lr.remove_object(crop.instance)
            lr.add_object_instance(instance)
            changes = True
        except Exception:
            import traceback

            traceback.print_exc()
            print(f"Response from model: {message.content[0].text}")

    # 7. Save Labels.
    if changes:
        lr.save()
