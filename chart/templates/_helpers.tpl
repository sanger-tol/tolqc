{{/*
Expand the name of the chart.
*/}}
{{- define "tolqc-app.name" -}}
{{- default .Chart.Name .Values.tolcore.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "tolqc-app.fullname" -}}
{{- if .Values.tolcore.fullnameOverride }}
{{- .Values.tolcore.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.tolcore.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
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
{{- if .Values.tolcore.serviceAccount.create }}
{{- default (include "tolqc-app.fullname" .) .Values.tolcore.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.tolcore.serviceAccount.name }}
{{- end }}
{{- end }}
