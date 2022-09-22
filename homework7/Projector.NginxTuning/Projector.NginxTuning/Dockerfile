FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build

WORKDIR /src
COPY ["Projector.NginxTuning/Projector.NginxTuning.csproj", "Projector.NginxTuning/"]
RUN dotnet restore "Projector.NginxTuning/Projector.NginxTuning.csproj"

COPY . .
WORKDIR "/src/Projector.NginxTuning"
RUN dotnet build "Projector.NginxTuning.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Projector.NginxTuning.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Projector.NginxTuning.dll"]
