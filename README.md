## IDS 721 Project 1 -- Cloud Continuous Delivery of Microservice -- Major City Info Finder



### Brief

In this project, a microservice is deployed for providing information of wanted major city including coordinate, population, belonging country and so on. 

### Feature

* Apply Flask micro-service framework on AWS EC2 Cloud Server

* Apply Github Action as build system to deploy changes

  ![image-20230120170454539](README.assets/image-20230120170454539.png)

* Apply AWS Cloud9 as IaC to deploy code

  <img src="README.assets/image-20230120170354341.png" alt="image-20230120170354341" style="zoom:50%;" />

### Usage

1. Get brief introduction of wanted city by inputing URL: http://ec2-3-86-15-81.compute-1.amazonaws.com/city/cityname. For example:
   * http://ec2-3-86-15-81.compute-1.amazonaws.com/city/newyork
     * New York is located at (latitude, longitude) 40.6943, -73.9249. It is in United States. New York has the population of 18713220.0.
   * http://ec2-3-86-15-81.compute-1.amazonaws.com/city/shanghai
     * Shanghai is located at (latitude, longitude) 31.1667, 121.4667. It is in China. Shanghai has the population of 22118000.0.