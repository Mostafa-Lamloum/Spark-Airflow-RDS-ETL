# The Amazon RDS Free Tier allows you to experiment with Amazon RDS for free.

Important: To avoid unnecessary charges, read the Amazon RDS Free Tier offering before launching any Amazon RDS resources.

## Resolution
**Steps**:
1. Open the Amazon RDS console.
3. In the navigation bar, select your Region from the Region selector.
4. In the **Create database** section, choose **Create database**.
5. For the Choose a database **creation method** section, choose **Standard create**.
6. In the **Engine options** section, select one of the following engine type: **MySQL**.
>Important: The Free Tier doesn't cover RDS DB instances launched with Amazon Aurora, Amazon RDS for Microsoft SQL Server, or Oracle database engines.
For Templates, select Free tier.
7. In the **Settings section**, enter the **DB instance identifier**, **Master username**, and **Master password**.
8. For **DB instance class, Storage, Connectivity, and Database authentication**, select the options that are best for your use case, or leave the default configurations.
>Note: Database authentication options are available only if you select MySQL.
9. Important: In the **Storage** section, clear **Enable storage autoscaling** to avoid incurring charges.
10. In the **Additional configuration** section, for **Initial database** name, enter a name for your database. For all other configuration details, choose the options that are best for your use case, or leave the default settings.
>Important: For Backup, clear **Enable automatic backups** to avoid incurring storage fees for retaining backups of your Amazon RDS instance.
11. Review the **Estimated monthly costs**, and then choose **Create database**.
12. Wait for a few minutes to make sure the instance is ready.
13. Go to the **RDS page**, and select **DB instances**.
14. Configure the **security group** inbound rules to allow your local machine's ip address.
15. Select your database and copy the **Endpoint** to your python script.
> This is the URL to your publicly accessible database instance for load_RDS.py script

## MySQL workbench connection setup

1. Open MySQL workbench
2. Select Create new connection
3. Add you RDS instance Endpoint, Username and password
4. Test the connection 
5. select Apply


## Reference 

[AWS Reference Link](https://repost.aws/knowledge-center/free-tier-rds-launch)
