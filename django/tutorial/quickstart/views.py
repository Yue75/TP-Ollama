import os
import shutil

from django.conf import settings
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from gradio_client import Client


def index(request):

    return render(
        request,
        "quickstart/index.html"
    )


@api_view(["POST"])
def generate_tts(request):

    try:

        text = request.data.get(
            "text",
            ""
        )

        speaker = request.data.get(
            "speaker",
            "emily"
        )

        emotion = request.data.get(
            "emotion",
            "neutral"
        )

        client = Client(
            "neuphonic/neutts-2e",
            token=os.environ["HF_TOKEN"]
        )

        audio = client.predict(

            gen_text=text,

            speaker=speaker,

            emotion=emotion,

            temperature=1,

            top_k=50,

            api_name="/infer"

        )

        os.makedirs(
            settings.MEDIA_ROOT,
            exist_ok=True
        )

        destination = os.path.join(

            settings.MEDIA_ROOT,

            "generated.wav"

        )

        shutil.copy(

            audio,

            destination

        )

        return Response({

            "audio_url":"/media/generated.wav"

        })

    except Exception as e:

        return Response({

            "error":str(e)

        },status=500)