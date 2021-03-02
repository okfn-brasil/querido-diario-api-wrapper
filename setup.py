from setuptools import setup

setup(
    name="querido_diario_api_wrapper",
    version="0.0.1",
    description="CLI for Querido Diário API",
    url="http://github.com/rennerocha/querido-diario-api-wrapper",
    author="Renne Rocha",
    author_email="renne@rocha.dev.br",
    license="MIT",
    packages=["querido_diario"],
    zip_safe=False,
    install_requires=["requests"],
)
