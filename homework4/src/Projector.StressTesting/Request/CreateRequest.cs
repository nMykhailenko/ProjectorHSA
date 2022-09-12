using System.Text.Json.Serialization;

namespace Projector.StressTesting.Request;

public record CreateRequest
{
    [JsonPropertyName("query")]
    public string Query { get; init; } = null!;
}