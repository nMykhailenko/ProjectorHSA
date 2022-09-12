using Microsoft.EntityFrameworkCore;
using Projector.StressTesting.Domain;

namespace Projector.StressTesting.Persistence;

public class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
    {
    }
    
    public DbSet<Domain.Request> Requests { get; set; } = null!;
}