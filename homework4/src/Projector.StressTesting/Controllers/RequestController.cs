using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Projector.StressTesting.Persistence;
using Projector.StressTesting.Request;

namespace Projector.StressTesting.Controllers;

[ApiController]
[Route("api/requests")]
public class RequestController : Controller
{
    private readonly ApplicationDbContext _context;

    public RequestController(ApplicationDbContext context)
    {
        _context = context;
    }

    [HttpGet]
    public async Task<IActionResult> Get()
    {
        var entities = await _context.Requests.ToListAsync();
        return Ok(entities);
    }

    [HttpPost]
    public async Task<IActionResult> Post([FromBody]CreateRequest request)
    {
        var entity = new Domain.Request {Query = request.Query};
        await _context.Requests.AddAsync(entity);
        await _context.SaveChangesAsync();

        return Ok(entity);
    }

}