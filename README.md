<br>

**Pollutants**

<br>

## Upcoming

Automation:

* From local machine to GitHub to Amazon Elastic Container Registry (Via GitHub Actions) .  This requires a few more settings 
  * [Open Identity](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services); also study the [news of changes](https://github.com/marketplace/actions/configure-aws-credentials-action-for-github-actions#oidc)
  * Re-visit the [old approach](https://towardsaws.com/build-push-docker-image-to-aws-ecr-using-github-actions-8396888a8f9e), and 
   the approach used for the planets project.  In relation the new approach [study this example](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-and-push-docker-images-to-amazon-ecr-using-github-actions-and-terraform.html), which is infeasible because Terraform is not an open source product anymore.
* Amazon Glue & Data Catalogues
* Code Analysis & GitHub Actions
* The Dockerfile for production state; [a production set-up example](https://github.com/discourses/augmentation/blob/master/Dockerfile).

Usage Notes:

- [ ] Explanatory usage notes
- [ ] Resources files


Mathematics:

* [Manifolds](https://scikit-learn.org/stable/modules/manifold.html)

<br>

## Explanatory Notes

To delete an Amazon Glue Crawler or Amazon Glue Database

> ```shell
> python src/glue/delete/main.py {item} {instance}
> ``` 

wherein {item} is an Amazon Glue item, at present {item} = <span style="color: #722f37">crawler</span> or <span style="color: #722f37">database</span>, and {instance} is the name of a crawler or a database. 

<br>



<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
