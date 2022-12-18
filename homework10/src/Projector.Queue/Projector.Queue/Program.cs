using System.Text.Json;
using Beanstalk.Core;
using ServiceStack.Messaging;
using ServiceStack.Redis;
using StackExchange.Redis;

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
    var connection = ConnectionMultiplexer.Connect("localhost:6379");
    var subscriber = connection.GetSubscriber();

    var email = new Email
    {
        from = "cs@greentimeinvestment.com",
        to = new List<string> {"mykyta.m@plat4me.com"},
        cc = new List<string>(),
        subject = "Test sender 3saving new",
        body =
            "<!DOCTYPE html>\n<html>\n    <head></head>\n<body>\n    <p>Welcome</p>\n-----\n  <p>Hi, this is test-1-1</p>  \n-----\n    <p>Contact me:  </p>\n    Best regards,\nVolodymyr Andryeyev\n</body>\n</html>",
        files = new List<object>(),
    };
    var root = new Root
    {
        email = email,
        extra = new Extra
        {
            conversationMessageId = 425
        }
    };
    await subscriber.PublishAsync("email", JsonSerializer.Serialize(root));
    // var redisManager = new RedisManagerPool("localhost:6380");
    // using var client = new RedisMessageProducer(redisManager);
    //
    // var user = new User(Guid.NewGuid().ToString(), Guid.NewGuid().ToString());
    // var messageAsStr = JsonSerializer.Serialize(user);
    // var message = new Message {Body = user};
    // client.Publish("projector", message);

    Console.WriteLine($"Put to redis-rdb message: {JsonSerializer.Serialize(root)}");
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

public class Email
{
    public string from { get; set; }
    public List<string> to { get; set; }
    public List<string> cc { get; set; }
    public List<object> bcc { get; set; }
    public string subject { get; set; }
    public string body { get; set; }
    public List<object> files { get; set; }
}

public class Extra
{
    public int conversationMessageId { get; set; }
}

public class Root
{
    public Email email { get; set; }
    public Extra extra { get; set; }
}