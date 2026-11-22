# import required modules
import python_weather
import asyncio


async def main() -> None:

  # Declare the client. The measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    # Fetch a weather forecast from a city.
    city = input(print("Enter city"))
    weather = await client.get(city)

    temperature = weather.temperature
    # Fetch the temperature for today.
    print(weather.temperature)
    print(temperature)
    if (temperature > 12):
        print("its greater than 12 allowed to wear light clothes ")
    else:
        print("its less than 12 only wear heavy packed clothes")
if __name__ == '__main__':
  asyncio.run(main())