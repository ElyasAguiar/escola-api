from fastapi_amis_admin import i18n
from fastapi_amis_admin.admin import admin
from fastapi_amis_admin.admin.settings import Settings
from fastapi_amis_admin.admin.site import AdminSite
from fastapi_amis_admin.amis.components import PageSchema

from app.core.config import settings
from app.database import engine
from start_point.models.models import Aluno, Professor, Titulo

i18n.set_language(language="en_US")

# Create AdminSite instance
site = AdminSite(settings=Settings(database_url=settings.DATABASE_URI), engine=engine)


# Registration management class
@site.register_admin
class GitHubIframeAdmin(admin.IframeAdmin):
    # Set page menu information
    page_schema = PageSchema(label="AmisIframeAdmin", icon="fa fa-github")
    # Set the jump link
    src = "https://google.com"


# register ModelAdmin
@site.register_admin
class AlunoAdmin(admin.ModelAdmin):
    page_schema = "Aluno"
    # set model
    model = Aluno


# register ModelAdmin
@site.register_admin
class TituloAdmin(admin.ModelAdmin):
    page_schema = "Titulo"
    # set model
    model = Titulo


# register ModelAdmin
@site.register_admin
class ProfessorAdmin(admin.ModelAdmin):
    page_schema = "Professor"
    # set model
    model = Professor
