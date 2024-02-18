<br>

**In Progress**

<br>

### Notes

**Continuous Integration, Delivery, Deployment**

Images & Containers
- [x] The Dockerfile for [development](/.devcontainer/Dockerfile).
- [x] The Dockerfile for [production](Dockerfile).
- [ ] A compose.yaml for local testing (<span style="color: #722f37">In Progress</span>)

<br>

Container Registries:
- [x] Local machine &rarr; GitHub &rarr; Amazon Elastic Container Registry (Via [GitHub Actions](.github/workflows/main.yml))
- [x] Local machine &rarr; GitHub &rarr; GitHub Container Registry (Via [GitHub Actions](.github/workflows/main.yml)) 

<br>

Cataloguing:
- [x] Cataloguing Amazon S3 (Simple Storage Service) deliveries via Amazon Glue (Via the Glue Package)

<br>

Code Analysis
- [ ] Code Analysis & GitHub Actions (<span style="color: #722f37">In Progress</span>)

<br>

Usage Notes:
- [ ] Explanatory usage notes
- [ ] Resources files

<br>

### Images & Containers

A simple option for image testing is a `compose.yaml`, especially if the image container has to interact with Amazon 
services.  <span style="color: #777777">The script ...</span> Subsequently, within the directory hosting `compose.yaml`

```shell
 docker pull ghcr.io/enqueter/pollutants:develop
 docker compose up -d
```

If there are any problems

```shell
docker compose logs -f
```

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
