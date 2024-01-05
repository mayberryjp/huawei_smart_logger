# Huawei Smart Logger 3000 Data Retrieval

This project queries data from a locally owned and operated Huawei Smart Logger 3000 used as part of the Huawei Fusion Solar system and outputs that data as a JSON KVP.

More information can be found [here](https://support.huawei.com/enterprise/en/doc/EDOC1100108365) and [here](https://support.huawei.com/enterprise/en/doc/EDOC1100108365/1a9e42de/webui-layout)

Example usage

```
from huawei_smart_logger import HuaweiSmartLogger3000API
import json
import asyncio

class Test():
    async def main(self):
        hsl = HuaweiSmartLogger3000API("admin","password","192.168.x.x")
        await hsl.fetch_data()
        data_dict = hsl.get_results()
        json_object = json.dumps(data_dict)
        print(json_object)

test=Test()
asyncio.run(test.main())

```

You should see an output like this

{"gridtied_active_power": "0.055", "gridtied_reactive_power": "0.332", "load_power": "1.070", "active_power": "1.015", "reactive_power": "-0.334", "todays_power_supply_from_grid": "0.00", "current_day_supply_from_grid": "5.47", "current_day_feedin_to_grid": "0.41", "current_day_consumption": "12.87", "total_power_supply_from_grid": "6.61", "total_supply_from_grid": "449.67", "total_feedin_to_grid": "555.87", "total_power_consumption": "1774.54", "pv_output_power": "2.855", "battery_chargedischarge_power": "1.840", "reactive_pv_power": "-0.334", "reactive_ess_power": "0.000", "soc": "97.0", "currentday_charge_capacity": "9.27", "currentday_discharge_capacity": "3.17", "total_charge": "819.04", "total_discharge": "811.73", "rated_ess_power": "0.000"}

