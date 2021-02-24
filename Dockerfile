ARG DOCKER_IMAGE_REGISTRY
FROM ${DOCKER_IMAGE_REGISTRY}/agatha/ds-base-flask:1.0.51

ARG DS_ASSEMBLY_TYPE=FLASK
ENV DS_ASSEMBLY_TYPE=${DS_ASSEMBLY_TYPE}
LABEL com.e451.agatha.ds_assembly_type=${DS_ASSEMBLY_TYPE}

ARG APP_GIT_HASH
ENV APP_GIT_HASH=${APP_GIT_HASH}

ENV GOOGLE_APPLICATION_CREDENTIALS=/oauth/auth.json
ENV GCS_AUTH_FILE=/oauth/auth.json

ARG SERVICE_PORT=5000
ENV SERVICE_PORT=${SERVICE_PORT}

ENV APP_DIR=/flask_app
ENV APP_DIR=${APP_DIR}

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

VOLUME ${APP_DIR}
COPY ./ ${APP_DIR}/
RUN if [ -f "${APP_DIR}/rlibs.R" ]; then R -f ${APP_DIR}/rlibs.R; fi

#App will run on port 5000
EXPOSE ${SERVICE_PORT}

ENV flask_app="app:app"
