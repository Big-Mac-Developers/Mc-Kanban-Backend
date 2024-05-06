# Build 


```
# Create venv
python3.8 -m venv env

# Activate venv mac/linux
source env/bin/activate
# Windows
.\env\Scripts\Activate.ps1 

# Install dependencies
pip install -r requirements.txt
```

### Add env variable
create .env file add the following values

```
SUPABASE_URL = <INSERT URL>
SUPABASE_KEY = <INSERT KEY>
ANTHROPIC_API_KEY = <INSERT KEY>
```

### Start fast api server
```
fastapi dev .\src\main.py 
```
or 
```
uvicorn src.main:app --reload 
```

### View api documentation 
http://localhost:8000/docs
