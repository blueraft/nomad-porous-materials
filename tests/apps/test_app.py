def test_importing_app():
    # this will raise an exception if pydantic model validation fails for the app
    from nomad_porous_materials.apps import mofapp

