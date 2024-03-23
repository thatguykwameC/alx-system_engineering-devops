## Web Infrastructure Design

This document outlines a secure and robust web infrastructure design for `www.foobar.com` It prioritizes security, encrypted traffic, and monitoring for optimal website performance and user experience.

### Components:

* Users
* Firewalls (x3) - Enhance security by filtering incoming and outgoing traffic
* Load Balancer (HAproxy) - Distributes user requests evenly across web servers
* Web Servers (Nginx) (x2) - Serve website content
* Application Server - Processes website logic and interacts with the database
* Application Files - Website codebase (location varies)
* Database (MySQL) - Stores website data (potentially with Primary-Replica Cluster)
* Monitoring Clients (x3) - Collect server performance and health data
* Data Collector - Sends collected data to a monitoring service (e.g., Sumo Logic)
