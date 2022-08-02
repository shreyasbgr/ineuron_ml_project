Setting up the ML project

```
conda create -p venv python==3.7 -y
conda activate venv/
```

Docker image -> Docker container
```
docker build -t ineuron-ml-project:latest .
docker images
docker run -p 5000:5000 -e PORT=5000 <image-id>
```

Stop Docker container
```
docker ps
docker stop <container-id>
```

VSCode Workspace settings.json file:
```
{
    "terminal.integrated.defaultProfile.windows": "Command Prompt",
    "python.PYTHONPATH": "C:\\Users\\shreyas.banagar\\OneDrive - Zycus\\iNeuron\\Repos\\ineuron_ml_project\\venv\\python.exe",
    "python.terminal.activateEnvironment": true,
}
```