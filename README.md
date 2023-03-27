# FastAPI
A python framework

link: https://www.youtube.com/playlist?list=PLqAmigZvYxIL9dnYeZEhMoHcoP4zop8-p

If you're running Linux or MacOS you'll instead run
```bash
conda create --name new_env_name python=3.10.9

conda activate new_env_name

conda install --file requirements.txt

```

If this still doesn't work, you can try using pip instead of conda to install the packages:

```bash
pip install -r requirements.txt
```
## Running the app
`uvicorn main:app --reload`