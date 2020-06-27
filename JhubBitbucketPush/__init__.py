from JhubBitbucketPush.handlers import setup_handlers
# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'JhubBitbucketPush',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "notebook",
        "dest": "JhubBitbucketPush",
        "src": "static",
        "require": "JhubBitbucketPush/main"
    }]

def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp.web_app)
