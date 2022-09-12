namespace Projector.StressTesting.Domain;

public class Request
{
    public long Id { get; set; }
    public string Query { get; set; } = null!;
}