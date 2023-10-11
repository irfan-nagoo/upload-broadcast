# upload-broadcast


![image](https://github.com/irfan-nagoo/upload-broadcast/assets/96521607/7bae1614-6030-4bd7-9814-a8d7966df30b)


This project is a sample application which can act as a digital media library (like Netflix) or media share point (like Youtube), and can potentially be used for other uses cases as well. The upload-broad-service provides APIs to upload and broadcast (or discover) media artifacts primarily videos/audios and images. This project is a vanilla application and could be extended to support many additional features. This project is fully written in Python programming language.


## Use Cases

This application could be used in many uses cases. Some of the primary use cases are:

1. As a media library to upload videos with cover images (done generally by admin) and a searchable discovery interface for users to explore and watch content.
2. As a share point where any user can upload the media content and any other user can search and watch that content.
3. As a event broadcast application in which a video of the event is recorded, uploaded to this application and becomes available to everyone through list/search APIs.
 

## REST APIs & Components

This application has two app components and one common component:
1. **Upload app:** This component handles upload of media (video/audio, image) and some other information related to the media is responsible for storing that information in the database and media files on the file store. This components also sends media events to Apache Kafka for indexing in the underlying search technology.
2. **Broadcast app:** This component exposes discovery APIs to search and discovery media content.
3. **Common:** This components contains some common classes and vendor specific implementations for messaging broker (Apache Kafka) and search technology (Apache Solr). Both Upload and Broadcast apps uses this component.


This application exposes following REST API:

1. Upload:
    - **Artifact Upload:** This application exposes endpoints to add/get/modify/delete media content. The add/modify/delete APIs also update the content in the underlying search technology.
2. Broadcast:
    - **Artifact List:** This application provides paginated and sorted APIs to list the media content with latest content at the top excluding deleted records. This API could generally be used in the home page of the frontend application. 
    - **Artifact Search:** This application provides paginated API to search content based on title, description etc.
3. Media content:
    - **Video/Image Uri:** These are static endpoints which get generated while video/image upload, and are unique for each media artifact. These URIs need to be prefixed with http://host:port  of broadcast-upload-service to access the media content.


### Extendibility

The PostGres database script is also included in this project. This application can work with any relational database. In additon to this, this application is configured to work with Apache Solr for searching and Apaache Kafka for messaging. However, these technologies could be replaced with other implementations as well with minimum code changes.

This project could be extended with features like user management (with User table), customized search APIs based on category, type etc., tables for tags, types, websocket notification, subscriptions, plans and payment info (if required) etc. with database tables as per requirement.


## Configuration

The default configuration for this application should work on local. This application requires following configuration before it could be started:

1. The media file location setup. This could be generally a network file system so that any instance of this application can access it. If its a cloud deployment, then we can also think about API based AWS S3 storage for media files.
2. PostGres database should be up and schema created.
3. Apache Solr should be up and running. 
4. Apache Kafka should be up with required topic created.



**Tech stack:** Python 3, Django 4, Django rest, urllib3, confluent-kafka, Apache Solr, Apache Kafka, PostGres


Here is the Swagger UI enpoint for various REST APIs: http://localhost:8080/swagger-ui

 
