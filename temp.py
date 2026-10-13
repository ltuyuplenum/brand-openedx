tutor_hooks.Filters.ENV_PATCHES.add_item(
    (
        "mfe-dockerfile-post-npm-install",
        """
RUN npm install '@edx/brand@git+https://github.com/ltuyuplenum/brand-openedx.git'
"""
    )
)