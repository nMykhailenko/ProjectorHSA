using System.Text.Json;
using Beanstalk.Core;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

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