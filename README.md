# wifi-upload
A tiny Flask app for transferring files in a pinch.

## Usage
```shell
python -m venv .env
source .env/bin/activate
pip install flask
flask run --debug --host 0.0.0.0 --port 8085
```
Visit `http://host.ip.addr:8085/` and upload files via the form. They will appear in `./uploads`.
