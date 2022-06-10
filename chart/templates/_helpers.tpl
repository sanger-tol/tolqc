{{/*
Expand the name of the chart.
*/}}
{{- define "tolqc-app.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "tolqc-app.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create a default fully qualified name for the API service.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "tolqc-app.api.fullname" -}}
{{- if .Values.api.fullname }}
{{- .Values.api.fullname | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create a default fully qualified name for the UI service.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "tolqc-app.ui.fullname" -}}
{{- if .Values.ui.fullname }}
{{- .Values.ui.fullname | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create a default fully qualified name for the DB service.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "tolqc-app.db.fullname" -}}
{{- if .Values.db.fullname }}
{{- .Values.db.fullname | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Fullname for alembic
*/}}
{{- define "tolqc-app.alembic.fullname" -}}
"tolqc-alembic"
{{- end }}

{{/*
Fullname for dbutils
*/}}
{{- define "tolqc-app.dbutils.fullname" -}}
"tolqc-dbutils"
{{- end }}

{{/*
Fullname for (dbutils) restore job
*/}}
{{- define "tolqc-app.restore.fullname" -}}
"tolqc-restore"
{{- end }}

{{/*
Fullname for (dbutils) backup pod
*/}}
{{- define "tolqc-app.backup.fullname" -}}
"tolqc-backup"
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "tolqc-app.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "tolqc-app.labels" -}}
helm.sh/chart: {{ include "tolqc-app.chart" . }}
{{ include "tolqc-app.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "tolqc-app.selectorLabels" -}}
app.kubernetes.io/name: {{ include "tolqc-app.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "tolqc-app.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "tolqc-app.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}

{{/*
Determine the DB port. This is, by default, 5432.
*/}}
{{- define "tolqc-app.db.port" -}}
{{- if eq .Values.db.port "" }}
{{- "5432" -}}
{{- else }}
{{- .Values.db.port -}}
{{- end }}
{{- end }}

{{/*
Determine the DB host. (always the db fullname for a cluster-local DB)
*/}}
{{- define "tolqc-app.db.host" -}}
{{- if eq .Values.db.create_local "true" -}}
{{- include "tolqc-app.db.fullname" . }}
{{- else }}
{{- .Values.db.host }}
{{- end }}
{{- end }}

{{/*
Build the DB connection URI from its constituent parts
*/}}
{{- define "tolqc-app.db.uri" -}}
{{- $dbuser := .Values.db.user }}
{{- $dbpassword := .Values.db.password }}
{{- $dbname := .Values.db.name }}
{{- $dbhost := (include "tolqc-app.db.host" .) }}
{{- $dbport := (include "tolqc-app.db.port" .) }}
{{- (printf "postgresql://%s:%s@%s:%s/%s" $dbuser $dbpassword $dbhost $dbport $dbname ) }}
{{- end }}

{{/*
Build the API image string from its constiuent parts
*/}}
{{- define "tolqc-app.api.image" -}}
{{- .Values.image.repository }}/{{ .Values.api.fullname }}:{{ .Values.image.tag | default .Chart.AppVersion }}
{{- end }}

{{/*
Build the dbutils image string from its constiuent parts
*/}}
{{- define "tolqc-app.dbutils.image" -}}
{{- .Values.dbutils.image.repository }}:{{- .Values.dbutils.image.tag }}
{{- end }}
