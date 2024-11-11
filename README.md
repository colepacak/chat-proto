## Set up virtual environment

```bash
python3 -m venv chat-env
source chat-env/bin/activate
```
Install dependencies
```bash
pip install openai
```

To deactivate the virtual environment, run:
```bash
deactivate
```

Set the OpenAI API key
```bash
export OPENAI_API_KEY=$(cat api-key.txt)
```

If you don't have a key, you can get one [here](https://platform.openai.com/api-keys).

## Running the script
To run the script, use the following command:
```bash
python3 main.py
```