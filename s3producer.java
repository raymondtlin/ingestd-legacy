	import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.PropertiesCredentials;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3Client;
import com.amazonaws.services.s3.model.Bucket;
import com.amazonaws.services.s3.model.DeleteObjectsRequest;
import com.amazonaws.services.s3.model.ObjectListing;
import com.amazonaws.services.s3.model.ObjectMetadata;
import com.amazonaws.services.s3.model.PutObjectResult;
import com.amazonaws.services.s3.model.S3Object;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.Arrays;

public class App {

    private static final Logger LOGGER = LoggerFactory.getLogger(App.class);

    private static final String BUCKET_NAME = "bhdrkn-backups";
    private static final String KEY = "mysql/mysql_backup.gzip";

    public static void main(String[] args) throws Exception {
        final InputStream properties = Thread.currentThread().getContextClassLoader().getResourceAsStream("aws.properties");
        final AWSCredentials propertiesCredentials = new PropertiesCredentials(properties);
        final AmazonS3 amazonS3 = new AmazonS3Client(propertiesCredentials);

        // Creating Bucket
        final Bucket bucket = amazonS3.createBucket(BUCKET_NAME);
        LOGGER.info("Bucket {} is created at {}.", bucket.getName(), bucket.getCreationDate());

        // Creating Item
        final byte[] bytes = "Hello, World".getBytes("UTF-8");
        final InputStream inputStream = new ByteArrayInputStream(bytes);
        final PutObjectResult putObjectResult = amazonS3.putObject(BUCKET_NAME, KEY, inputStream, new ObjectMetadata());
        LOGGER.info("Object is saved! Etag [{}] ", putObjectResult.getETag());

        // Reading Item
        final S3Object object = amazonS3.getObject(BUCKET_NAME, KEY);
        final InputStream objectContent = object.getObjectContent();
        final byte[] objectBytes = new byte[1024];
        final int read = objectContent.read(objectBytes);
        final String helloWorld = new String(Arrays.copyOfRange(objectBytes, 0, read));
        LOGGER.info("Data is read from S3 '{}'", helloWorld);

        // Listing Item Information
        final ObjectListing mysql = amazonS3.listObjects(BUCKET_NAME, "mysql");
        mysql.getObjectSummaries().stream().forEach(s3ObjectSummary -> LOGGER.info("S3 Object: ", s3ObjectSummary.getKey()));

        // Deleting Items
        amazonS3.deleteObjects(new DeleteObjectsRequest(BUCKET_NAME).withKeys(KEY));

        // Deleting Bucket
        amazonS3.deleteBucket(BUCKET_NAME);
    }
}