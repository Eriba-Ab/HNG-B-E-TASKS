from datetime import datetime
import pytz
import json
from django.http import HttpResponse

def hng0_api(request):
    data = {
        "email": "eribainc@gmail.com",
        "current_datetime": datetime.now(pytz.utc).isoformat(),
        "github_url": "https://github.com/Eriba-Ab/HNG-B-E-TASKS"
    }
    # Convert to a JSON string with indentation
    pretty_data = json.dumps(data, indent=2)
    return HttpResponse(pretty_data, content_type="application/json")

