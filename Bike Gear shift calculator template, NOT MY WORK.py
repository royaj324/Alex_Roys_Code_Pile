<!--
    Application Name: Gear Ratio Calculator
    Course: Powertrain MECH 4313
    Name: Mohamad Amirullah bin Rahman
    Matric No: 1714115
-->

<html>
    <title>Gear Ratio Calculator</title>
</head>

<body style="background: #F032C7;
background: -webkit-linear-gradient(top left, #F032C7, #21D6E4);
background: -moz-linear-gradient(top left, #F032C7, #21D6E4);
background: linear-gradient(to bottom right, #F032C7, #21D6E4);
color:rgb(0, 0, 0);font-family:cursive;">
    <center>
        <form id="gearRatio" action="">
            <fieldset>
                <center>
                    <legend>Gear Ratio Calculator</legend>
                </center>
                <!--Input value for driving gear teeth-->
                <p>
                    <label for="drivingGear2">Driving Gear Teeth</label><br>
                    <input id="drivingGear2" name="drivingGear2" type="number" />
                </p>
                <!--Input value for driven gear teeth-->
                <p>
                    <label for="drivenGear1">Driven Gear Teeth</label><br>
                    <input id="drivenGear1" name="drivenGear1" type="number" />
                </p><br>
                <p>
                    <input class="myButton" type="submit" value="Calculate Ratio" />
                    <input class="myButton" type="reset" value="Reset" />
                </p><br>
                    <label for="ratio">Gear Ratio</label><br>
                    <input id="ratio" name="ratio" />
                </p>
            </fieldset>
        </form>
    </center>
<script>
    (function() {
        function calculateRatio(drivenGear1, drivingGear2)
        {
            drivenGear1 = parseFloat(drivenGear1);
            drivingGear2 = parseFloat(drivingGear2);
            return (drivingGear2 / drivenGear1);
        }

        var form = document.getElementById("gearRatio");
        if (form) {
            form.onsubmit = function() {
            this.ratio.value = calculateRatio(this.drivenGear1.value, this.drivingGear2.value);
            return false;
            };
        }
    }());
</script>
<style>
    .myButton
    {
	box-shadow: 0px 10px 14px -7px #3e7327;
	background:linear-gradient(to bottom, #77b55a 5%, #72b352 100%);
	background-color:#77b55a;
	border-radius:4px;
	border:1px solid #60d127;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:13px;
	font-weight:bold;
	padding:6px 12px;
	text-decoration:none;
	text-shadow:0px 1px 0px #5b8a3c;
    }
    .myButton:hover
    {
        background:linear-gradient(to bottom, #72b352 5%, #77b55a 100%);
        background-color:#72b352;
    }
    .myButton:active
    {
        position:relative;
        top:1px;
    }
</style>
</body>
</html>