# Chatbook Test
## How to run
1. Add your twitter credentials to `.env` file besides docker-compose file.
   The content should look like
   ```
   TWITER_API_KEY='api_key'
   TWITER_API_SECRET_KEY='secret_key'
   TWITER_BEARER_TOKEN='bearer_token'
   TWITER_ACCESS_TOKEN='access_token'
   TWITER_ACCESS_TOKEN_SECRET='access_token_secret'
   ```

2. Then run the docker compose command to start server
    ```
    docker-compose up -d
    ```

3. Import the postman collection and run the APIs.


## Data in Redis
We are saving the tweet ids in redis and not the text.
As a key value pair we are saving key as user id + current epoch time and value is tweet id.
Ex: 
Consider user id is `id123`. We will store data in redis as

```
"id123_1619102331361" -> 238748752524398
"id123_1619102331362" -> 238974978324773
"id123_1619102331363" -> 729834861928738
"id123_1619102331364" -> 378127128379146
```
### Check the data in redis
1. Find the docker container id or name which is probably `chatbook-test_redis_1`.
2. Login into container ` docker exec -it chatbook-test_redis_1 /bin/sh`
3. Run the cli with `redis-cli` command
4. Run command `KEYS *`. You will see all the keys.
5. Run `GET key` to get the data.

## How APIs work
#### New Tweet api (POST /api/v1/twitter/tweets/)
1. Update status(tweet) in twitter and get the id

2. Save the id with current time onto redis

3. Return the id and text

#### Get tweets api (GET /api/v1/twitter/tweets/)
1. Get all keys of the user. Currently we have added user is as `user`.
   So fetch `keys user*`

2. Sort keys by decending order

3. Get the first 10 keys and fetch ids from redis

4. Using this ids, fetch the tweet data from twitter

5. Parse the data and return to user
