[GTA Plugin](https://github.com/crosire/scripthookvdotnet)
An ASI plugin for Grand Theft Auto V, which allows running scripts written in any .NET language in-game.


[DeepGTAV v2](https://github.com/aitorzip/DeepGTAV)
[Angelapper Fork](https://github.com/angelapper/DeepGTAV.git)
A plugin for GTAV that transforms it into a vision-based self-driving car research environment.

[reward and lane information](https://github.com/aitorzip/DeepGTAV/issues/8)


Speed (m/s)
Acceleration (m/s2)
Brake pedal position (0 to 1)
Steering angle (-1 to 1, left to right)
Throttle pedal position (-1 to 1, negative is reverse)
Yaw rate (deg/s)
Direction (-1 to left, 1 to right)

### steering, throttle, brake issue, verion have to match
here is the way to fix
https://github.com/aitorzip/DeepGTAV/issues/3
https://github.com/aitorzip/DeepGTAV/issues/43
0x8D4, 0x8FC
0x8D8, 0x900
0x8CC, 0x8F4

Steering Angle: 0x8AC or 0x89C
Throttle: 0x8B4 or 0x8A4
Brake: 0x8B8 or 0x8A8

void Scenario::setThrottle(){
	d["throttle"] = getFloatValue(vehicle, 0x92C);
}

void Scenario::setBrake(){
	d["brake"] = getFloatValue(vehicle, 0x930);
}

void Scenario::setSteering(){
	d["steering"] = getFloatValue(vehicle, 0x924) / -0.7;
}

[GTAV Universe](https://github.com/OSSDC/deepdrive-universe)