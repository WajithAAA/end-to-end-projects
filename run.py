import os
from app import create_app

app = create_app('testing')
current_dir = os.getcwd()


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 3345)), debug=False)
