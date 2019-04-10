# Research.fi API
## Environment setup
### Add configuration file .env
Configuration file **.env** must be manually added into the project root. Otherwise the Docker containers cannot be launched. The file should define these environment variables:

* DJANGO_ENV_ELASTICSEARCH_HOST
  * Hostname/IP and port of the Elasticsearch API
* DJANGO_ENV_SECRET_KEY
  * For local development any random string is fine.
  * https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-SECRET_KEY

Here is an example of the file content.

```
DJANGO_ENV_ELASTICSEARCH_HOST=http://10.143.5.31:9200
DJANGO_ENV_SECRET_KEY=a7h3d2387hasd6gsad
```
