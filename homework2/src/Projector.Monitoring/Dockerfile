FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["Projector.Monitoring/Projector.Monitoring.csproj", "Projector.Monitoring/"]
RUN dotnet restore "Projector.Monitoring/Projector.Monitoring.csproj"
COPY . .
WORKDIR "/src/Projector.Monitoring"
RUN dotnet build "Projector.Monitoring.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Projector.Monitoring.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Projector.Monitoring.dll"]
