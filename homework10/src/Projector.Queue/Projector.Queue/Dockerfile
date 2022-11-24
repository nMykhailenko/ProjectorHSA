FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /src
COPY ["Projector.Queue/Projector.Queue.csproj", "Projector.Queue/"]
RUN dotnet restore "Projector.Queue/Projector.Queue.csproj"
COPY . .
WORKDIR "/src/Projector.Queue"
RUN dotnet build "Projector.Queue.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Projector.Queue.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Projector.Queue.dll"]
