# dpps

![Version: 0.0.0-dev](https://img.shields.io/badge/Version-0.0.0--dev-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.0.0-dev](https://img.shields.io/badge/AppVersion-0.0.0--dev-informational?style=flat-square)

A Helm chart for the DPPS project

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| The DPPS Authors |  |  |

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://fluent.github.io/helm-charts | fluent-bit | 0.48.9 |
| https://grafana.github.io/helm-charts | grafana | 9.2.2 |
| https://grafana.github.io/helm-charts | loki | 6.30.1 |
| https://prometheus-community.github.io/helm-charts | prometheus | 27.20.0 |
| oci://harbor.cta-observatory.org/dpps | bdms | v0.4.1 |
| oci://harbor.cta-observatory.org/dpps | cert-generator-grid | v3.1.0 |
| oci://harbor.cta-observatory.org/dpps | wms | v0.4.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| bdms.cert-generator-grid.enabled | bool | `false` |  |
| bdms.configure_test_setup | bool | `true` |  |
| bdms.enabled | bool | `true` | Whether to deploy BDMS |
| bdms.iam.bootstrap.config.clients[0].client_id | string | `"dpps-test-client"` |  |
| bdms.iam.bootstrap.config.clients[0].client_name | string | `"WMS Test Client"` |  |
| bdms.iam.bootstrap.config.clients[0].client_secret | string | `"secret"` |  |
| bdms.iam.bootstrap.config.clients[0].grant_types[0] | string | `"authorization_code"` |  |
| bdms.iam.bootstrap.config.clients[0].grant_types[1] | string | `"password"` |  |
| bdms.iam.bootstrap.config.clients[0].grant_types[2] | string | `"client_credentials"` |  |
| bdms.iam.bootstrap.config.clients[0].grant_types[3] | string | `"urn:ietf:params:oauth:grant_type:redelegate"` |  |
| bdms.iam.bootstrap.config.clients[0].grant_types[4] | string | `"refresh_token"` |  |
| bdms.iam.bootstrap.config.clients[0].scopes[0] | string | `"scim:write"` |  |
| bdms.iam.bootstrap.config.clients[0].scopes[1] | string | `"scim:read"` |  |
| bdms.iam.bootstrap.config.clients[0].scopes[2] | string | `"offline_access"` |  |
| bdms.iam.bootstrap.config.clients[0].scopes[3] | string | `"openid"` |  |
| bdms.iam.bootstrap.config.clients[0].scopes[4] | string | `"profile"` |  |
| bdms.iam.bootstrap.config.clients[0].scopes[5] | string | `"iam:admin.write"` |  |
| bdms.iam.bootstrap.config.clients[0].scopes[6] | string | `"iam:admin.read"` |  |
| bdms.iam.bootstrap.config.env[0].name | string | `"X509_NON_DPPS_USER_CERT"` |  |
| bdms.iam.bootstrap.config.env[0].value | string | `"/tmp/user-non-dpps-cert.pem"` |  |
| bdms.iam.bootstrap.config.env[1].name | string | `"X509_UNPRIVILEGED_DPPS_USER_CERT"` |  |
| bdms.iam.bootstrap.config.env[1].value | string | `"/tmp/user-unprivileged-cert.pem"` |  |
| bdms.iam.bootstrap.config.image.pullPolicy | string | `"IfNotPresent"` |  |
| bdms.iam.bootstrap.config.image.repository | string | `"harbor.cta-observatory.org/dpps/dpps-iam-client"` |  |
| bdms.iam.bootstrap.config.image.tag | string | `nil` |  |
| bdms.iam.bootstrap.config.issuer | string | `"http://wms-dpps-iam-login-service:8080"` |  |
| bdms.iam.bootstrap.config.tag | string | `nil` |  |
| bdms.iam.bootstrap.config.users[0].cert.default_path | string | `"/tmp/usercert.pem"` |  |
| bdms.iam.bootstrap.config.users[0].cert.env_var | string | `"X509_USER_CERT"` |  |
| bdms.iam.bootstrap.config.users[0].cert.kind | string | `"env_var_file"` |  |
| bdms.iam.bootstrap.config.users[0].email | string | `"dpps@test.example"` |  |
| bdms.iam.bootstrap.config.users[0].family_name | string | `"User"` |  |
| bdms.iam.bootstrap.config.users[0].given_name | string | `"DPPS"` |  |
| bdms.iam.bootstrap.config.users[0].groups[0] | string | `"ctao.dpps.test"` |  |
| bdms.iam.bootstrap.config.users[0].groups[1] | string | `"dpps_group"` |  |
| bdms.iam.bootstrap.config.users[0].groups[2] | string | `"dpps_genpilot"` |  |
| bdms.iam.bootstrap.config.users[0].groups[3] | string | `"dirac_admin"` |  |
| bdms.iam.bootstrap.config.users[0].groups[4] | string | `"dirac_user"` |  |
| bdms.iam.bootstrap.config.users[0].password | string | `"dpps-password"` |  |
| bdms.iam.bootstrap.config.users[0].role | string | `"ROLE_USER"` |  |
| bdms.iam.bootstrap.config.users[0].subject_dn | string | `"DPPS User"` |  |
| bdms.iam.bootstrap.config.users[0].username | string | `"dpps_user"` |  |
| bdms.iam.bootstrap.config.users[1].cert.default_path | string | `"/tmp/usercert.pem"` |  |
| bdms.iam.bootstrap.config.users[1].cert.env_var | string | `"X509_USER_CERT"` |  |
| bdms.iam.bootstrap.config.users[1].cert.kind | string | `"env_var_file"` |  |
| bdms.iam.bootstrap.config.users[1].email | string | `"dpps@test.example"` |  |
| bdms.iam.bootstrap.config.users[1].family_name | string | `"User"` |  |
| bdms.iam.bootstrap.config.users[1].given_name | string | `"TestDpps"` |  |
| bdms.iam.bootstrap.config.users[1].groups[0] | string | `"ctao.dpps.test"` |  |
| bdms.iam.bootstrap.config.users[1].groups[1] | string | `"dpps_group"` |  |
| bdms.iam.bootstrap.config.users[1].groups[2] | string | `"dirac_user"` |  |
| bdms.iam.bootstrap.config.users[1].password | string | `"test-password"` |  |
| bdms.iam.bootstrap.config.users[1].role | string | `"ROLE_USER"` |  |
| bdms.iam.bootstrap.config.users[1].subject_dn | string | `"DPPS User"` |  |
| bdms.iam.bootstrap.config.users[1].username | string | `"test_user"` |  |
| bdms.iam.bootstrap.config.users[2].email | string | `"dpps@test.example"` |  |
| bdms.iam.bootstrap.config.users[2].family_name | string | `"User"` |  |
| bdms.iam.bootstrap.config.users[2].given_name | string | `"TestAdmin"` |  |
| bdms.iam.bootstrap.config.users[2].groups[0] | string | `"ctao.dpps.test"` |  |
| bdms.iam.bootstrap.config.users[2].password | string | `"test-password"` |  |
| bdms.iam.bootstrap.config.users[2].role | string | `"ROLE_ADMIN"` |  |
| bdms.iam.bootstrap.config.users[2].username | string | `"admin-user"` |  |
| bdms.iam.bootstrap.extraVolumes[0].name | string | `"dppsuser-certkey"` |  |
| bdms.iam.bootstrap.extraVolumes[0].secret.defaultMode | int | `272` |  |
| bdms.iam.bootstrap.extraVolumes[0].secret.secretName | string | `"dpps-dppsuser-certkey"` |  |
| bdms.iam.bootstrap.extraVolumes[1].name | string | `"dppsuser-certkey-600"` |  |
| bdms.iam.bootstrap.extraVolumes[1].secret.defaultMode | int | `384` |  |
| bdms.iam.bootstrap.extraVolumes[1].secret.secretName | string | `"dpps-dppsuser-certkey"` |  |
| bdms.iam.bootstrap.extraVolumes[2].name | string | `"dppsuser-certkey-400"` |  |
| bdms.iam.bootstrap.extraVolumes[2].secret.defaultMode | int | `256` |  |
| bdms.iam.bootstrap.extraVolumes[2].secret.secretName | string | `"dpps-dppsuser-certkey"` |  |
| bdms.iam.bootstrap.extraVolumes[3].name | string | `"dppsuser-unprivileged-certkey"` |  |
| bdms.iam.bootstrap.extraVolumes[3].secret.defaultMode | int | `272` |  |
| bdms.iam.bootstrap.extraVolumes[3].secret.secretName | string | `"dpps-dppsuser-unprivileged-certkey"` |  |
| bdms.iam.bootstrap.extraVolumes[4].name | string | `"dppsuser-unprivileged-certkey-600"` |  |
| bdms.iam.bootstrap.extraVolumes[4].secret.defaultMode | int | `384` |  |
| bdms.iam.bootstrap.extraVolumes[4].secret.secretName | string | `"dpps-dppsuser-unprivileged-certkey"` |  |
| bdms.iam.bootstrap.extraVolumes[5].name | string | `"dppsuser-unprivileged-certkey-400"` |  |
| bdms.iam.bootstrap.extraVolumes[5].secret.defaultMode | int | `256` |  |
| bdms.iam.bootstrap.extraVolumes[5].secret.secretName | string | `"dpps-dppsuser-unprivileged-certkey"` |  |
| bdms.iam.bootstrap.extraVolumes[6].name | string | `"dppsuser-non-dpps-certkey"` |  |
| bdms.iam.bootstrap.extraVolumes[6].secret.defaultMode | int | `272` |  |
| bdms.iam.bootstrap.extraVolumes[6].secret.secretName | string | `"dpps-dppsuser-non-dpps-certkey"` |  |
| bdms.iam.bootstrap.extraVolumes[7].name | string | `"dppsuser-non-dpps-certkey-600"` |  |
| bdms.iam.bootstrap.extraVolumes[7].secret.defaultMode | int | `384` |  |
| bdms.iam.bootstrap.extraVolumes[7].secret.secretName | string | `"dpps-dppsuser-non-dpps-certkey"` |  |
| bdms.iam.bootstrap.extraVolumes[8].name | string | `"dppsuser-non-dpps-certkey-400"` |  |
| bdms.iam.bootstrap.extraVolumes[8].secret.defaultMode | int | `256` |  |
| bdms.iam.bootstrap.extraVolumes[8].secret.secretName | string | `"dpps-dppsuser-non-dpps-certkey"` |  |
| bdms.iam.cert-generator-grid.enabled | bool | `false` |  |
| bdms.iam.dev.mount_repo | bool | `false` |  |
| bdms.iam.enabled | bool | `true` |  |
| bdms.iam.fullnameOverride | string | `"dpps-iam"` |  |
| bdms.iam.iam.database.external.existingSecret | string | `""` |  |
| bdms.iam.iam.database.external.host | string | `"dpps-mariadb"` |  |
| bdms.iam.iam.database.external.name | string | `"indigo-iam"` |  |
| bdms.iam.iam.database.external.password | string | `"PassW0rd"` |  |
| bdms.iam.iam.database.external.port | int | `3306` |  |
| bdms.iam.iam.database.external.username | string | `"indigo-iam"` |  |
| bdms.iam.iam.fullnameOverride | string | `"dpps-iam"` |  |
| bdms.iam.iam.mariadb.enabled | bool | `false` |  |
| bdms.iam.iam.mysql.enabled | bool | `false` |  |
| bdms.rucio_iam_sync_user.iam_server | string | `"http://dpps-iam-login-service:8080"` |  |
| bdms.safe_to_bootstrap_rucio | bool | `true` |  |
| cert-generator-grid.enabled | bool | `true` |  |
| cert-generator-grid.extra_server_names[0] | string | `"iam.test.example"` |  |
| cert-generator-grid.extra_server_names[1] | string | `"voms.test.example"` |  |
| cert-generator-grid.extra_server_names[2] | string | `"rucio-storage-1"` |  |
| cert-generator-grid.extra_server_names[3] | string | `"rucio-storage-2"` |  |
| cert-generator-grid.extra_server_names[4] | string | `"rucio-storage-3"` |  |
| cert-generator-grid.extra_server_names[5] | string | `"fts"` |  |
| cert-generator-grid.extra_server_names[6] | string | `"dirac-server"` |  |
| cert-generator-grid.generatePreHooks | bool | `true` |  |
| cert-generator-grid.users[0].name | string | `"DPPS User"` |  |
| cert-generator-grid.users[0].suffix | string | `""` |  |
| cert-generator-grid.users[1].name | string | `"DPPS User Unprivileged"` |  |
| cert-generator-grid.users[1].suffix | string | `"-unprivileged"` |  |
| cert-generator-grid.users[2].name | string | `"Non-DPPS User"` |  |
| cert-generator-grid.users[2].suffix | string | `"-non-dpps"` |  |
| dev.client_image_tag | string | `nil` | tag of the image used to run helm tests |
| dev.mount_repo | bool | `true` | mount the repo volume to test the code as it is being developed |
| dev.n_test_jobs | int | `1` | number of parallel test jobs for pytest |
| dev.pipelines | object | `{"calibpipe":{"version":"v0.2.0"},"datapipe":{"version":"v0.2.1"}}` | Pipelines versions used in the tests |
| dev.runAsGroup | int | `1000` |  |
| dev.runAsUser | int | `1000` | user to run the container as. needs to be the same as local user if writing to repo directory |
| dev.run_tests | bool | `true` | run tests in the container |
| dev.sleep | bool | `false` | sleep after test to allow interactive development |
| dev.start_long_running_client | bool | `false` | if true, a long-running client container will start *instead* of a test container |
| fluent-bit.config.inputs | string | `"[INPUT]\n    Name tail\n    Path /var/log/containers/*.log\n    multiline.parser docker, cri\n    Tag kube.*\n    Mem_Buf_Limit 5MB\n    Buffer_Chunk_Size 1\n    Refresh_Interval 1\n    Skip_Long_Lines On\n"` |  |
| fluent-bit.config.outputs | string | `"[FILTER]\n    Name grep\n    Match *\n\n[OUTPUT]\n    Name        loki\n    Match       *\n    Host        dpps-loki-gateway\n    port        80\n    tls         off\n    tls.verify  off\n"` |  |
| fluent-bit.config.rbac.create | bool | `true` |  |
| fluent-bit.config.rbac.eventsAccess | bool | `true` |  |
| fluent-bit.enabled | bool | `true` |  |
| fluent-bit.image.repository | string | `"harbor.cta-observatory.org/proxy_cache/fluent/fluent-bit"` |  |
| fluent-bit.testFramework.image.repository | string | `"harbor.cta-observatory.org/proxy_cache/busybox"` |  |
| global.image.registry | string | `"harbor.cta-observatory.org/proxy_cache"` |  |
| global.registry | string | `"harbor.cta-observatory.org/proxy_cache"` |  |
| global.security.allowInsecureImages | bool | `true` |  |
| grafana.adminPassword | string | `"admin"` |  |
| grafana.adminUser | string | `"admin"` |  |
| grafana.dashboardProviders."dashboardproviders.yaml".apiVersion | int | `1` |  |
| grafana.dashboardProviders."dashboardproviders.yaml".providers[0].editable | bool | `true` |  |
| grafana.dashboardProviders."dashboardproviders.yaml".providers[0].name | string | `"default"` |  |
| grafana.dashboardProviders."dashboardproviders.yaml".providers[0].options.path | string | `"/var/lib/grafana/dashboards/default"` |  |
| grafana.dashboardProviders."dashboardproviders.yaml".providers[0].type | string | `"file"` |  |
| grafana.dashboardProviders."dashboardproviders.yaml".providers[1].editable | bool | `true` |  |
| grafana.dashboardProviders."dashboardproviders.yaml".providers[1].name | string | `"sidecar"` |  |
| grafana.dashboardProviders."dashboardproviders.yaml".providers[1].options.path | string | `"/var/lib/grafana/dashboards/sidecar"` |  |
| grafana.dashboardProviders."dashboardproviders.yaml".providers[1].type | string | `"file"` |  |
| grafana.dashboards.default.k8-views-global.datasource | string | `"Prometheus"` |  |
| grafana.dashboards.default.k8-views-global.gnetId | int | `15757` |  |
| grafana.dashboards.default.k8-views-global.revision | int | `43` |  |
| grafana.dashboards.default.k8-views-namespaces.datasource | string | `"Prometheus"` |  |
| grafana.dashboards.default.k8-views-namespaces.gnetId | int | `15758` |  |
| grafana.dashboards.default.k8-views-namespaces.revision | int | `42` |  |
| grafana.dashboards.default.k8-views-nodes.datasource | string | `"Prometheus"` |  |
| grafana.dashboards.default.k8-views-nodes.gnetId | int | `15759` |  |
| grafana.dashboards.default.k8-views-nodes.revision | int | `37` |  |
| grafana.dashboards.default.k8-views-pods.datasource | string | `"Prometheus"` |  |
| grafana.dashboards.default.k8-views-pods.gnetId | int | `15760` |  |
| grafana.dashboards.default.k8-views-pods.revision | int | `36` |  |
| grafana.datasources."datasources.yaml".apiVersion | int | `1` |  |
| grafana.datasources."datasources.yaml".datasources[0].access | string | `"proxy"` |  |
| grafana.datasources."datasources.yaml".datasources[0].name | string | `"Prometheus"` |  |
| grafana.datasources."datasources.yaml".datasources[0].type | string | `"prometheus"` |  |
| grafana.datasources."datasources.yaml".datasources[0].url | string | `"http://dpps-prometheus-server"` |  |
| grafana.datasources."datasources.yaml".datasources[1].access | string | `"proxy"` |  |
| grafana.datasources."datasources.yaml".datasources[1].jsonData.maxLines | int | `1000` |  |
| grafana.datasources."datasources.yaml".datasources[1].jsonData.timeout | int | `60` |  |
| grafana.datasources."datasources.yaml".datasources[1].name | string | `"Loki"` |  |
| grafana.datasources."datasources.yaml".datasources[1].type | string | `"loki"` |  |
| grafana.datasources."datasources.yaml".datasources[1].url | string | `"http://dpps-loki:3100"` |  |
| grafana.enabled | bool | `true` |  |
| grafana.image.registry | string | `"harbor.cta-observatory.org/proxy_cache"` |  |
| grafana.ingress.enabled | bool | `true` |  |
| grafana.ingress.hosts[0] | string | `"grafana.dpps.local"` |  |
| grafana.persistentVolume.size | string | `"100Mi"` |  |
| grafana.prometheus-node-exporter.enabled | bool | `false` |  |
| grafana.retention | string | `"1d"` |  |
| grafana.sidecar.dashboards.defaultFolderName | string | `"Sidecar Dashboards"` |  |
| grafana.sidecar.dashboards.enabled | bool | `true` |  |
| grafana.sidecar.dashboards.folder | string | `"/var/lib/grafana/dashboards/sidecar"` |  |
| grafana.sidecar.dashboards.folderAnnotation | string | `"grafana_folder"` |  |
| grafana.sidecar.dashboards.provider.name | string | `"sidecar"` |  |
| grafana.sidecar.dashboards.searchNamespace | string | `"ALL"` |  |
| grafana.sidecar.image.registry | string | `"harbor.cta-observatory.org/proxy_cache"` |  |
| grafana.testFramework.enabled | bool | `false` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository_prefix | string | `"harbor.cta-observatory.org/dpps/dpps"` |  |
| loki.backend.replicas | int | `0` |  |
| loki.bloomCompactor.replicas | int | `0` |  |
| loki.bloomGateway.replicas | int | `0` |  |
| loki.compactor.replicas | int | `0` |  |
| loki.deploymentMode | string | `"SingleBinary"` |  |
| loki.distributor.replicas | int | `0` |  |
| loki.enabled | bool | `true` |  |
| loki.indexGateway.replicas | int | `0` |  |
| loki.ingester.replicas | int | `0` |  |
| loki.loki.auth_enabled | bool | `false` |  |
| loki.loki.commonConfig.replication_factor | int | `1` |  |
| loki.loki.limits_config.allow_structured_metadata | bool | `true` |  |
| loki.loki.limits_config.volume_enabled | bool | `true` |  |
| loki.loki.pattern_ingester.enabled | bool | `true` |  |
| loki.loki.ruler.enable_api | bool | `true` |  |
| loki.loki.schemaConfig.configs[0].from | string | `"2024-04-01"` |  |
| loki.loki.schemaConfig.configs[0].index.period | string | `"24h"` |  |
| loki.loki.schemaConfig.configs[0].index.prefix | string | `"loki_index_"` |  |
| loki.loki.schemaConfig.configs[0].object_store | string | `"s3"` |  |
| loki.loki.schemaConfig.configs[0].schema | string | `"v13"` |  |
| loki.loki.schemaConfig.configs[0].store | string | `"tsdb"` |  |
| loki.loki.storage.bucketNames.admin | string | `"loki-admin"` |  |
| loki.loki.storage.bucketNames.chunks | string | `"loki-chunks"` |  |
| loki.loki.storage.bucketNames.ruler | string | `"loki-ruler"` |  |
| loki.loki.storage.s3.accessKeyId | string | `"rootuser"` |  |
| loki.loki.storage.s3.endpoint_url | string | `"http://dpps-minio:9000"` |  |
| loki.loki.storage.s3.insecure | bool | `true` |  |
| loki.loki.storage.s3.s3ForcePathStyle | bool | `true` |  |
| loki.loki.storage.s3.secretAccessKey | string | `"rootpass123"` |  |
| loki.loki.storage.type | string | `"s3"` |  |
| loki.memcached.image.repository | string | `"harbor.cta-observatory.org/proxy_cache/memcached"` |  |
| loki.memcached.image.tag | string | `"1.6.38-alpine3.22"` |  |
| loki.minio.enabled | bool | `false` |  |
| loki.monitoring.selfMonitoring.enabled | bool | `false` |  |
| loki.monitoring.selfMonitoring.grafanaAgent.installOperator | bool | `false` |  |
| loki.monitoring.selfMonitoring.lokiCanary.enabled | bool | `false` |  |
| loki.querier.replicas | int | `0` |  |
| loki.queryFrontend.replicas | int | `0` |  |
| loki.queryScheduler.replicas | int | `0` |  |
| loki.read.replicas | int | `0` |  |
| loki.rollout_operator.enabled | bool | `false` |  |
| loki.singleBinary.replicas | int | `1` |  |
| loki.test.enabled | bool | `false` |  |
| loki.write.replicas | int | `0` |  |
| prometheus.alertmanager.enabled | bool | `false` |  |
| prometheus.enabled | bool | `true` |  |
| prometheus.prometheus-node-exporter.image.registry | string | `"harbor.cta-observatory.org/proxy_cache"` |  |
| prometheus.prometheus-node-exporter.image.repository | string | `"prom/node-exporter"` |  |
| prometheus.prometheus-pushgateway.enabled | bool | `false` |  |
| prometheus.server.image.repository | string | `"harbor.cta-observatory.org/proxy_cache/prom/prometheus"` |  |
| wms.cert-generator-grid.enabled | bool | `false` |  |
| wms.cvmfs.enabled | bool | `true` |  |
| wms.cvmfs.publish_docker_images[0] | string | `"harbor.cta-observatory.org/dpps/datapipe:v0.2.1"` |  |
| wms.cvmfs.publish_docker_images[1] | string | `"harbor.cta-observatory.org/dpps/calibpipe:v0.2.0"` |  |
| wms.dirac_server.configmap.create | bool | `false` |  |
| wms.diracx.developer.enabled | bool | `true` |  |
| wms.diracx.developer.localCSPath | string | `"/local_cs_store"` |  |
| wms.diracx.developer.urls.diracx | string | `"http://dpps-diracx:8000"` |  |
| wms.diracx.developer.urls.iam | string | `"http://dpps-iam:8080"` |  |
| wms.diracx.developer.urls.minio | string | `"http://dpps-minio:32000"` |  |
| wms.diracx.dex.enabled | bool | `false` |  |
| wms.diracx.diracx.hostname | string | `"dpps-diracx"` |  |
| wms.diracx.diracx.osDbs.dbs.JobParametersDB | string | `nil` |  |
| wms.diracx.diracx.settings.DIRACX_CONFIG_BACKEND_URL | string | `"git+file:///cs_store/initialRepo"` |  |
| wms.diracx.diracx.settings.DIRACX_LEGACY_EXCHANGE_HASHED_API_KEY | string | `"19628aa0cb14b69f75b2164f7fda40215be289f6e903d1acf77b54caed61a720"` |  |
| wms.diracx.diracx.settings.DIRACX_SANDBOX_STORE_AUTO_CREATE_BUCKET | string | `"true"` |  |
| wms.diracx.diracx.settings.DIRACX_SANDBOX_STORE_BUCKET_NAME | string | `"sandboxes"` |  |
| wms.diracx.diracx.settings.DIRACX_SANDBOX_STORE_S3_CLIENT_KWARGS | string | `"{\"endpoint_url\": \"http://dpps-minio:9000\", \"aws_access_key_id\": \"rootuser\", \"aws_secret_access_key\": \"rootpass123\"}"` |  |
| wms.diracx.diracx.settings.DIRACX_SERVICE_AUTH_ACCESS_TOKEN_EXPIRE_MINUTES | string | `"120"` |  |
| wms.diracx.diracx.settings.DIRACX_SERVICE_AUTH_ALLOWED_REDIRECTS | string | `"[\"http://dpps-diracx:8000/api/docs/oauth2-redirect\", \"http://dpps-diracx:8000/#authentication-callback\"]"` |  |
| wms.diracx.diracx.settings.DIRACX_SERVICE_AUTH_REFRESH_TOKEN_EXPIRE_MINUTES | string | `"360"` |  |
| wms.diracx.diracx.settings.DIRACX_SERVICE_AUTH_TOKEN_ISSUER | string | `"http://dpps-diracx:8000"` |  |
| wms.diracx.diracx.settings.DIRACX_SERVICE_AUTH_TOKEN_KEYSTORE | string | `"file:///keystore/jwks.json"` |  |
| wms.diracx.diracx.sqlDbs.dbs.AuthDB.internalName | string | `"DiracXAuthDB"` |  |
| wms.diracx.diracx.sqlDbs.dbs.JobDB | string | `nil` |  |
| wms.diracx.diracx.sqlDbs.dbs.JobLoggingDB | string | `nil` |  |
| wms.diracx.diracx.sqlDbs.dbs.SandboxMetadataDB | string | `nil` |  |
| wms.diracx.diracx.sqlDbs.dbs.TaskQueueDB | string | `nil` |  |
| wms.diracx.diracx.sqlDbs.default.host | string | `"dirac-db:3306"` |  |
| wms.diracx.diracx.sqlDbs.default.password | string | `"dirac-db"` |  |
| wms.diracx.diracx.sqlDbs.default.rootPassword | string | `"dirac-db-root"` |  |
| wms.diracx.diracx.sqlDbs.default.rootUser | string | `"root"` |  |
| wms.diracx.diracx.sqlDbs.default.user | string | `"Dirac"` |  |
| wms.diracx.diracx.startupProbe.failureThreshold | int | `60` |  |
| wms.diracx.diracx.startupProbe.periodSeconds | int | `15` |  |
| wms.diracx.diracx.startupProbe.timeoutSeconds | int | `5` |  |
| wms.diracx.elasticsearch.enabled | bool | `false` |  |
| wms.diracx.enabled | bool | `true` |  |
| wms.diracx.global.activeDeadlineSeconds | int | `900` |  |
| wms.diracx.global.batchJobTTL | int | `3600` |  |
| wms.diracx.global.imagePullPolicy | string | `"Always"` |  |
| wms.diracx.global.images.client | string | `"ghcr.io/diracgrid/diracx/client"` |  |
| wms.diracx.global.images.services | string | `"ghcr.io/diracgrid/diracx/services"` |  |
| wms.diracx.global.images.tag | string | `"v0.0.1a50"` |  |
| wms.diracx.grafana.enabled | bool | `false` |  |
| wms.diracx.indigoiam.enabled | bool | `false` |  |
| wms.diracx.initSql.enabled | bool | `false` |  |
| wms.diracx.initSql.env | object | `{}` |  |
| wms.diracx.jaeger.enabled | bool | `false` |  |
| wms.diracx.minio.environment.MINIO_BROWSER_REDIRECT_URL | string | `"http://dpps-minio:32001/"` |  |
| wms.diracx.minio.rootPassword | string | `"rootpass123"` |  |
| wms.diracx.minio.rootUser | string | `"rootuser"` |  |
| wms.diracx.mysql.enabled | bool | `false` |  |
| wms.diracx.opensearch.enabled | bool | `true` |  |
| wms.diracx.opentelemetry-collector.enabled | bool | `false` |  |
| wms.diracx.prometheus.enabled | bool | `false` |  |
| wms.diracx.rabbitmq.auth.existingErlangSecret | string | `"rabbitmq-secret"` |  |
| wms.diracx.rabbitmq.auth.existingPasswordSecret | string | `"rabbitmq-secret"` |  |
| wms.diracx.rabbitmq.containerSecurityContext.enabled | bool | `false` |  |
| wms.diracx.rabbitmq.enabled | bool | `true` |  |
| wms.diracx.rabbitmq.image.registry | string | `"harbor.cta-observatory.org/proxy_cache"` |  |
| wms.diracx.rabbitmq.image.repository | string | `"bitnamilegacy/rabbitmq"` |  |
| wms.diracx.rabbitmq.podSecurityContext.enabled | bool | `false` |  |
| wms.enabled | bool | `true` | Whether to deploy WMS |
| wms.global.dockerRegistry | string | `"harbor.cta-observatory.org/proxy_cache"` |  |
| wms.global.images.busybox.repository | string | `"harbor.cta-observatory.org/proxy_cache/busybox"` |  |
| wms.global.registry | string | `"harbor.cta-observatory.org/proxy_cache"` |  |
| wms.iam.bootstrap.extraVolumeMounts[0].mountPath | string | `"/tmp/userkey.pem"` |  |
| wms.iam.bootstrap.extraVolumeMounts[0].name | string | `"dppsuser-certkey-400"` |  |
| wms.iam.bootstrap.extraVolumeMounts[0].subPath | string | `"dppsuser.key.pem"` |  |
| wms.iam.bootstrap.extraVolumeMounts[1].mountPath | string | `"/tmp/usercert.pem"` |  |
| wms.iam.bootstrap.extraVolumeMounts[1].name | string | `"dppsuser-certkey-600"` |  |
| wms.iam.bootstrap.extraVolumeMounts[1].subPath | string | `"dppsuser.pem"` |  |
| wms.iam.bootstrap.extraVolumes[0].name | string | `"dppsuser-certkey"` |  |
| wms.iam.bootstrap.extraVolumes[0].secret.defaultMode | int | `272` |  |
| wms.iam.bootstrap.extraVolumes[0].secret.secretName | string | `"dpps-dppsuser-certkey"` |  |
| wms.iam.bootstrap.extraVolumes[1].name | string | `"dppsuser-certkey-600"` |  |
| wms.iam.bootstrap.extraVolumes[1].secret.defaultMode | int | `384` |  |
| wms.iam.bootstrap.extraVolumes[1].secret.secretName | string | `"dpps-dppsuser-certkey"` |  |
| wms.iam.bootstrap.extraVolumes[2].name | string | `"dppsuser-certkey-400"` |  |
| wms.iam.bootstrap.extraVolumes[2].secret.defaultMode | int | `256` |  |
| wms.iam.bootstrap.extraVolumes[2].secret.secretName | string | `"dpps-dppsuser-certkey"` |  |
| wms.iam.enabled | bool | `false` |  |
| wms.iam.fullnameOverride | string | `"dpps-iam"` |  |
| wms.iam.iam.fullnameOverride | string | `"dpps-iam"` |  |
| wms.iam.iam.global.registry | string | `"harbor.cta-observatory.org/proxy_cache"` |  |
| wms.iam.iam.waitForLoginService.image.pullPolicy | string | `"IfNotPresent"` |  |
| wms.iam.iam.waitForLoginService.image.repository | string | `"almalinux"` |  |
| wms.iam.iam.waitForLoginService.image.tag | int | `9` |  |
| wms.iamConfig.clients[0].client_id | string | `"dpps-test-client"` |  |
| wms.iamConfig.clients[0].client_name | string | `"WMS Test Client"` |  |
| wms.iamConfig.clients[0].client_secret | string | `"secret"` |  |
| wms.iamConfig.clients[0].grant_types[0] | string | `"authorization_code"` |  |
| wms.iamConfig.clients[0].grant_types[1] | string | `"password"` |  |
| wms.iamConfig.clients[0].grant_types[2] | string | `"client_credentials"` |  |
| wms.iamConfig.clients[0].grant_types[3] | string | `"urn:ietf:params:oauth:grant_type:redelegate"` |  |
| wms.iamConfig.clients[0].grant_types[4] | string | `"refresh_token"` |  |
| wms.iamConfig.clients[0].redirect_uris[0] | string | `"http://dpps-diracx:8000/api/auth/device/complete"` |  |
| wms.iamConfig.clients[0].redirect_uris[1] | string | `"http://dpps-diracx:8000/api/auth/authorize/complete"` |  |
| wms.iamConfig.clients[0].scopes[0] | string | `"scim:write"` |  |
| wms.iamConfig.clients[0].scopes[1] | string | `"scim:read"` |  |
| wms.iamConfig.clients[0].scopes[2] | string | `"offline_access"` |  |
| wms.iamConfig.clients[0].scopes[3] | string | `"openid"` |  |
| wms.iamConfig.clients[0].scopes[4] | string | `"profile"` |  |
| wms.iamConfig.clients[0].scopes[5] | string | `"iam:admin.write"` |  |
| wms.iamConfig.clients[0].scopes[6] | string | `"iam:admin.read"` |  |
| wms.iamConfig.groups.dirac_admin.user[0] | string | `"dpps_user"` |  |
| wms.iamConfig.groups.dirac_user.user[0] | string | `"test_user"` |  |
| wms.iamConfig.groups.dpps_genpilot.user[0] | string | `"dpps_user"` |  |
| wms.iamConfig.groups.dpps_group.user[0] | string | `"dpps_user"` |  |
| wms.iamConfig.groups.dpps_group.user[1] | string | `"test_user"` |  |
| wms.iamConfig.issuer | string | `"http://dpps-iam-login-service:8080"` |  |
| wms.iamConfig.users[0].cert.default_path | string | `"/tmp/usercert.pem"` |  |
| wms.iamConfig.users[0].cert.env_var | string | `"X509_USER_CERT"` |  |
| wms.iamConfig.users[0].cert.kind | string | `"env_var_file"` |  |
| wms.iamConfig.users[0].email | string | `"dpps@test.example"` |  |
| wms.iamConfig.users[0].family_name | string | `"User"` |  |
| wms.iamConfig.users[0].given_name | string | `"DPPS"` |  |
| wms.iamConfig.users[0].groups[0] | string | `"ctao.dpps.test"` |  |
| wms.iamConfig.users[0].groups[1] | string | `"dpps_group"` |  |
| wms.iamConfig.users[0].groups[2] | string | `"dpps_genpilot"` |  |
| wms.iamConfig.users[0].groups[3] | string | `"dirac_admin"` |  |
| wms.iamConfig.users[0].groups[4] | string | `"dirac_user"` |  |
| wms.iamConfig.users[0].password | string | `"dpps-password"` |  |
| wms.iamConfig.users[0].role | string | `"ROLE_USER"` |  |
| wms.iamConfig.users[0].subject_dn | string | `"DPPS User"` |  |
| wms.iamConfig.users[0].username | string | `"dpps_user"` |  |
| wms.iamConfig.users[1].cert.default_path | string | `"/tmp/usercert.pem"` |  |
| wms.iamConfig.users[1].cert.env_var | string | `"X509_USER_CERT"` |  |
| wms.iamConfig.users[1].cert.kind | string | `"env_var_file"` |  |
| wms.iamConfig.users[1].email | string | `"dpps@test.example"` |  |
| wms.iamConfig.users[1].family_name | string | `"User"` |  |
| wms.iamConfig.users[1].given_name | string | `"TestDpps"` |  |
| wms.iamConfig.users[1].groups[0] | string | `"ctao.dpps.test"` |  |
| wms.iamConfig.users[1].groups[1] | string | `"dpps_group"` |  |
| wms.iamConfig.users[1].groups[2] | string | `"dirac_user"` |  |
| wms.iamConfig.users[1].password | string | `"test-password"` |  |
| wms.iamConfig.users[1].role | string | `"ROLE_USER"` |  |
| wms.iamConfig.users[1].subject_dn | string | `"DPPS User"` |  |
| wms.iamConfig.users[1].username | string | `"test_user"` |  |
| wms.iamConfig.users[2].email | string | `"dpps@test.example"` |  |
| wms.iamConfig.users[2].family_name | string | `"User"` |  |
| wms.iamConfig.users[2].given_name | string | `"TestAdmin"` |  |
| wms.iamConfig.users[2].groups[0] | string | `"ctao.dpps.test"` |  |
| wms.iamConfig.users[2].password | string | `"test-password"` |  |
| wms.iamConfig.users[2].role | string | `"ROLE_ADMIN"` |  |
| wms.iamConfig.users[2].username | string | `"admin-user"` |  |
| wms.iam_external.enabled | bool | `true` |  |
| wms.iam_external.loginServiceURL | string | `"http://dpps-iam-login-service:8080"` |  |
| wms.mariadb.auth.rootPassword | string | `"dirac-db-root"` |  |
| wms.mariadb.enabled | bool | `true` |  |
| wms.mariadb.image.registry | string | `"harbor.cta-observatory.org/proxy_cache"` |  |
| wms.mariadb.image.repository | string | `"bitnamilegacy/mariadb"` |  |
| wms.mariadb.initdbScripts."create-user.sql" | string | `"CREATE USER IF NOT EXISTS 'Dirac'@'%' IDENTIFIED BY 'dirac-db';\nCREATE USER IF NOT EXISTS 'indigo-iam'@'%' IDENTIFIED BY 'PassW0rd';\nCREATE DATABASE IF NOT EXISTS `indigo-iam`;\nGRANT ALL PRIVILEGES ON `indigo-iam`.* TO `indigo-iam`@`%`;\nFLUSH PRIVILEGES;\n"` |  |
| wms.rucio.enabled | bool | `true` |  |
| wms.rucio.rucioConfig | string | `"dpps-bdms-rucio-config"` |  |

