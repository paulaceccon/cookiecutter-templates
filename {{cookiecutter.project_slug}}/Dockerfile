FROM python:{{ cookiecutter.python_version.rsplit('.', 1)[0] }}-slim as base

RUN     apt-get update && apt-get install -y \
        make \
        git \
        libgeos-dev \
    &&  pip3 install --upgrade pip \
    &&  rm -rf /var/lib/apt/lists/*

#########################
FROM base as intermediate
WORKDIR /pip-packages/
ADD Makefile requirements.txt setup.cfg setup.py README.md ./
ARG INSTALL_SUFFIX=""
RUN make "download${INSTALL_SUFFIX}"
RUN rm Makefile requirements.txt setup.cfg setup.py README.md

#########################

FROM base as final
COPY --from=intermediate /pip-packages/ /pip-packages/
RUN ls  /pip-packages/
RUN pip3 install --no-index --find-links=/pip-packages/ /pip-packages/*
WORKDIR /opt/project
ADD Makefile ./
COPY {{cookiecutter.project_slug}} ./{{cookiecutter.project_slug}}
CMD ["python", "-m", "{{cookiecutter.project_slug}}.main"]