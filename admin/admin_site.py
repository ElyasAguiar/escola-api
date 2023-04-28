from sqlalchemy import create_engine
from app.database import engine
from starlette_admin.contrib.sqla import Admin, ModelView

# from start_point.models.models import Aluno


def start_admin(app):
    # Create admin
    admin = Admin(engine)

    # Add view
    # admin.add_view(ModelView(Post))

    # Mount admin to your app
    admin.mount_to(app)
