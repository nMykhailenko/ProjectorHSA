using System.Text.Json;
using Beanstalk.Core;
using ServiceStack.Messaging;
using ServiceStack.Redis;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/redis-aof", async () => 
{
    var redisManager = new RedisManagerPool("localhost:6381");
    var redisFactory = new RedisMessageFactory(redisManager);
    using var client = redisFactory.CreateMessageQueueClient();

    var message = client.Get<User>("projector");
    Console.WriteLine($"Get data from redis-aof queue: {JsonSerializer.Serialize(message.GetBody())}");
});

app.MapPost("/redis-aof", async () => 
{
    var redisManager = new RedisManagerPool("localhost:6381");
    using var client = new RedisMessageProducer(redisManager);

    var user = new User(Guid.NewGuid().ToString(), Guid.NewGuid().ToString());
    var messageAsStr = JsonSerializer.Serialize(user);
    var message = new Message {Body = user};
    client.Publish("projector", message);

    Console.WriteLine($"Put to redis-aof message: {messageAsStr}");
});


app.MapGet("/redis-rdb", async () => 
{
    var redisManager = new RedisManagerPool("localhost:6380");
    var redisFactory = new RedisMessageFactory(redisManager);
    using var client = redisFactory.CreateMessageQueueClient();

    var message = client.Get<User>("projector");
    Console.WriteLine($"Get data from redis-rdb queue: {JsonSerializer.Serialize(message.GetBody())}");
});

app.MapPost("/redis-rdb", async () => 
{
    var redisManager = new RedisManagerPool("localhost:6380");
    using var client = new RedisMessageProducer(redisManager);

    var user = new User(Guid.NewGuid().ToString(), Guid.NewGuid().ToString());
    var messageAsStr = JsonSerializer.Serialize(user);
    var message = new Message {Body = user};
    client.Publish("projector", message);

    Console.WriteLine($"Put to redis-rdb message: {message}");
});


app.MapGet("/beanstalkd", async () =>
{
    using var client = new BeanstalkConnection("localhost", 11300);
    var job = await client.Reserve();
    Console.WriteLine($"Get data from beanstalkd queue: {job.Data}");
});

app.MapPost("/beanstalkd", async () =>
{
    using var client = new BeanstalkConnection("localhost", 11300);
    var message = new {id = Guid.NewGuid().ToString(), name = Guid.NewGuid().ToString()};
    var messageAsStr = JsonSerializer.Serialize(message);
    await client.Put(messageAsStr);
    Console.WriteLine($"Put to beanstalkd message: {message}");
});


app.Run();

public record User(string Id, string Name);