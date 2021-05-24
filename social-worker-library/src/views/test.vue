<template>
    <div class="test">
        <div id="container"></div>
        <v-btn
                :disabled="leading"
                :loading="leading"

                @click="ini()"
                class="mx-auto"
                color="#ECEFF1"
                elevation="4"
                large
                width="100px"
        >查找
        </v-btn>
    </div>

</template>

<script>
    import G6 from '@antv/g6';
    import url from "../components/url";

    export default {
        mounted() {
            this.graph = this.initComponent();
        },
        data() {
            return {
                msg: "",
                chart: null,
                globalHttpUrl: url.httpUrl,
                leading: false,
                warncard: false,
                happy: false,
                result: {
    "code": 200,
    "msg": "successful!",
    "result_data": {
        "edges": [
            {
                "source": "QQNum:100000",
                "target": "QunNum:20025566",
                "value": 1
            },
            {
                "source": "QQNum:100000",
                "target": "QunNum:20059682",
                "value": 1
            },
            {
                "source": "QQNum:100000",
                "target": "QunNum:30084997",
                "value": 1
            },
            {
                "source": "QQNum:100000",
                "target": "QunNum:932145",
                "value": 1
            },
            {
                "source": "QQNum:100000",
                "target": "QunNum:988810",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:100000",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:109320460",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:11011069",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:114824187",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:116136342",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:120733347",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:121340463",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:125036152",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:130004600",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:13108757",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:251153128",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:26590802",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:26659440",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:27201048",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:33032130",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:34460511",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:34781859",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:35783511",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:39928570",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:405915576",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:41131998",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:41636634",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:42295287",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:442190990",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:450459444",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:453406757",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:45869842",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:46441534",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:47637682",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:47806092",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:48999402",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:49023633",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:51731123",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:520039345",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:55790383",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:563477417",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:57143487",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:57296897",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:57545731",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:57602236",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:75492822",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:764731426",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:76885152",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:7789513",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:85537545",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:879504324",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:8833250",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:888888",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:970190109",
                "value": 1
            },
            {
                "source": "QunNum:20025566",
                "target": "QQNum:99328126",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:100000",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:243485682",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:285306062",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:330219985",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:345279146",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:346093802",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:379034431",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:415879901",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:504523551",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:516822314",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:517398439",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:532272331",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:640595342",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:654014044",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:75812591",
                "value": 1
            },
            {
                "source": "QunNum:20059682",
                "target": "QQNum:762133202",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:100000",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:200000",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:200730082",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:200892613",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:243508740",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:26919126",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:294404987",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:297183460",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:300000",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:308015274",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:337934627",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:343937090",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:393391583",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:397678912",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:400000",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:408934138",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:491828974",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:500000",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:525321435",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:532998334",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:546054621",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:549384276",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:584643897",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:598733008",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:600000",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:644723605",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:700000",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:739983900",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:748139333",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:758810096",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:800000",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:807922095",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:815751507",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:819579741",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:823860591",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:83663647",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:857066092",
                "value": 1
            },
            {
                "source": "QunNum:30084997",
                "target": "QQNum:900000",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:100000",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:10000000",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:100001",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:10271",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:10817",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:10916",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:10927",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:10937",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:11110",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:11114",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:11213",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:11999",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:1234567",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:14444",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:200000",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:21111",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:22221",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:22224",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:22225",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:300000",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:30303030",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:33331",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:33332",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:33334",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:33335",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:33336",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:33337",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:33338",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:37777",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:400000",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:43210",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:44000",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:44440",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:44441",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:444444",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:44445",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:44446",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:44447",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:44448",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:45555",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:49999",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:500000",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:51111",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:54444",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:55551",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:55552",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:55554",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:555555",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:55556",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:55557",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:55588",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:600000",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:619951999",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:62222",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:64444",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:65432",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:66661",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:66663",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:66667",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:66669",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:67777",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:700000",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:71111",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:72222",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:73333",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:74444",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:77770",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:77771",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:77772",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:77773",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:77775",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:77776",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:77778",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:77779",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:78888",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:800000",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:81111",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:82222",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:83333",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:84444",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:85630",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:88788",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:88800",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:88884",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:88885",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:88887",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:888888",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:900000",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:92222",
                "value": 1
            },
            {
                "source": "QunNum:932145",
                "target": "QQNum:99000",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:100000",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:10671",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:11110",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:11515151",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:188889851",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:200000",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:22221",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:22224",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:22225",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:28985",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:2898555",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:289855555",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:2898588",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:28991",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:28997",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:28999",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:300000",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:33133",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:33331",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:33335",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:33336",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:400000",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:4444344",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:444444",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:500000",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:52033991",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:555555",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:58686",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:600000",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:62000",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:67777",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:68686",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:700000",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:78888",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:800000",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:82000",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:888888",
                "value": 1
            },
            {
                "source": "QunNum:988810",
                "target": "QQNum:900000",
                "value": 1
            }
        ],
        "nodes": [
            {
                "id": "QQNum:100000",
                "key": "QQNum",
                "label": "QQNum:100000",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#ffff00",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QunNum:20025566",
                "key": "QQNum",
                "label": "QunNum:20025566",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#ff4081",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "rect",
                "value": "100000"
            },
            {
                "id": "QunNum:20059682",
                "key": "QQNum",
                "label": "QunNum:20059682",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#ff4081",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "rect",
                "value": "100000"
            },
            {
                "id": "QunNum:30084997",
                "key": "QQNum",
                "label": "QunNum:30084997",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#ff4081",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "rect",
                "value": "100000"
            },
            {
                "id": "QunNum:932145",
                "key": "QQNum",
                "label": "QunNum:932145",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#ff4081",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "rect",
                "value": "100000"
            },
            {
                "id": "QunNum:988810",
                "key": "QQNum",
                "label": "QunNum:988810",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#ff4081",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "rect",
                "value": "100000"
            },
            {
                "id": "QQNum:109320460",
                "key": "QQNum",
                "label": "QQNum:109320460",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:11011069",
                "key": "QQNum",
                "label": "QQNum:11011069",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:114824187",
                "key": "QQNum",
                "label": "QQNum:114824187",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:116136342",
                "key": "QQNum",
                "label": "QQNum:116136342",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:120733347",
                "key": "QQNum",
                "label": "QQNum:120733347",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:121340463",
                "key": "QQNum",
                "label": "QQNum:121340463",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:125036152",
                "key": "QQNum",
                "label": "QQNum:125036152",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:130004600",
                "key": "QQNum",
                "label": "QQNum:130004600",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:13108757",
                "key": "QQNum",
                "label": "QQNum:13108757",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:251153128",
                "key": "QQNum",
                "label": "QQNum:251153128",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:26590802",
                "key": "QQNum",
                "label": "QQNum:26590802",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:26659440",
                "key": "QQNum",
                "label": "QQNum:26659440",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:27201048",
                "key": "QQNum",
                "label": "QQNum:27201048",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:33032130",
                "key": "QQNum",
                "label": "QQNum:33032130",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:34460511",
                "key": "QQNum",
                "label": "QQNum:34460511",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:34781859",
                "key": "QQNum",
                "label": "QQNum:34781859",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:35783511",
                "key": "QQNum",
                "label": "QQNum:35783511",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:39928570",
                "key": "QQNum",
                "label": "QQNum:39928570",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:405915576",
                "key": "QQNum",
                "label": "QQNum:405915576",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:41131998",
                "key": "QQNum",
                "label": "QQNum:41131998",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:41636634",
                "key": "QQNum",
                "label": "QQNum:41636634",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:42295287",
                "key": "QQNum",
                "label": "QQNum:42295287",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:442190990",
                "key": "QQNum",
                "label": "QQNum:442190990",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:450459444",
                "key": "QQNum",
                "label": "QQNum:450459444",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:453406757",
                "key": "QQNum",
                "label": "QQNum:453406757",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:45869842",
                "key": "QQNum",
                "label": "QQNum:45869842",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:46441534",
                "key": "QQNum",
                "label": "QQNum:46441534",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:47637682",
                "key": "QQNum",
                "label": "QQNum:47637682",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:47806092",
                "key": "QQNum",
                "label": "QQNum:47806092",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:48999402",
                "key": "QQNum",
                "label": "QQNum:48999402",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:49023633",
                "key": "QQNum",
                "label": "QQNum:49023633",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:51731123",
                "key": "QQNum",
                "label": "QQNum:51731123",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:520039345",
                "key": "QQNum",
                "label": "QQNum:520039345",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:55790383",
                "key": "QQNum",
                "label": "QQNum:55790383",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:563477417",
                "key": "QQNum",
                "label": "QQNum:563477417",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:57143487",
                "key": "QQNum",
                "label": "QQNum:57143487",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:57296897",
                "key": "QQNum",
                "label": "QQNum:57296897",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:57545731",
                "key": "QQNum",
                "label": "QQNum:57545731",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:57602236",
                "key": "QQNum",
                "label": "QQNum:57602236",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:75492822",
                "key": "QQNum",
                "label": "QQNum:75492822",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:764731426",
                "key": "QQNum",
                "label": "QQNum:764731426",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:76885152",
                "key": "QQNum",
                "label": "QQNum:76885152",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:7789513",
                "key": "QQNum",
                "label": "QQNum:7789513",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:85537545",
                "key": "QQNum",
                "label": "QQNum:85537545",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:879504324",
                "key": "QQNum",
                "label": "QQNum:879504324",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:8833250",
                "key": "QQNum",
                "label": "QQNum:8833250",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:888888",
                "key": "QQNum",
                "label": "QQNum:888888",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:970190109",
                "key": "QQNum",
                "label": "QQNum:970190109",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:99328126",
                "key": "QQNum",
                "label": "QQNum:99328126",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:243485682",
                "key": "QQNum",
                "label": "QQNum:243485682",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:285306062",
                "key": "QQNum",
                "label": "QQNum:285306062",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:330219985",
                "key": "QQNum",
                "label": "QQNum:330219985",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:345279146",
                "key": "QQNum",
                "label": "QQNum:345279146",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:346093802",
                "key": "QQNum",
                "label": "QQNum:346093802",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:379034431",
                "key": "QQNum",
                "label": "QQNum:379034431",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:415879901",
                "key": "QQNum",
                "label": "QQNum:415879901",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:504523551",
                "key": "QQNum",
                "label": "QQNum:504523551",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:516822314",
                "key": "QQNum",
                "label": "QQNum:516822314",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:517398439",
                "key": "QQNum",
                "label": "QQNum:517398439",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:532272331",
                "key": "QQNum",
                "label": "QQNum:532272331",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:640595342",
                "key": "QQNum",
                "label": "QQNum:640595342",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:654014044",
                "key": "QQNum",
                "label": "QQNum:654014044",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:75812591",
                "key": "QQNum",
                "label": "QQNum:75812591",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:762133202",
                "key": "QQNum",
                "label": "QQNum:762133202",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:200000",
                "key": "QQNum",
                "label": "QQNum:200000",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:200730082",
                "key": "QQNum",
                "label": "QQNum:200730082",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:200892613",
                "key": "QQNum",
                "label": "QQNum:200892613",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:243508740",
                "key": "QQNum",
                "label": "QQNum:243508740",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:26919126",
                "key": "QQNum",
                "label": "QQNum:26919126",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:294404987",
                "key": "QQNum",
                "label": "QQNum:294404987",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:297183460",
                "key": "QQNum",
                "label": "QQNum:297183460",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:300000",
                "key": "QQNum",
                "label": "QQNum:300000",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:308015274",
                "key": "QQNum",
                "label": "QQNum:308015274",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:337934627",
                "key": "QQNum",
                "label": "QQNum:337934627",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:343937090",
                "key": "QQNum",
                "label": "QQNum:343937090",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:393391583",
                "key": "QQNum",
                "label": "QQNum:393391583",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:397678912",
                "key": "QQNum",
                "label": "QQNum:397678912",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:400000",
                "key": "QQNum",
                "label": "QQNum:400000",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:408934138",
                "key": "QQNum",
                "label": "QQNum:408934138",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:491828974",
                "key": "QQNum",
                "label": "QQNum:491828974",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:500000",
                "key": "QQNum",
                "label": "QQNum:500000",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:525321435",
                "key": "QQNum",
                "label": "QQNum:525321435",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:532998334",
                "key": "QQNum",
                "label": "QQNum:532998334",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:546054621",
                "key": "QQNum",
                "label": "QQNum:546054621",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:549384276",
                "key": "QQNum",
                "label": "QQNum:549384276",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:584643897",
                "key": "QQNum",
                "label": "QQNum:584643897",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:598733008",
                "key": "QQNum",
                "label": "QQNum:598733008",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:600000",
                "key": "QQNum",
                "label": "QQNum:600000",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:644723605",
                "key": "QQNum",
                "label": "QQNum:644723605",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:700000",
                "key": "QQNum",
                "label": "QQNum:700000",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:739983900",
                "key": "QQNum",
                "label": "QQNum:739983900",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:748139333",
                "key": "QQNum",
                "label": "QQNum:748139333",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:758810096",
                "key": "QQNum",
                "label": "QQNum:758810096",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:800000",
                "key": "QQNum",
                "label": "QQNum:800000",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:807922095",
                "key": "QQNum",
                "label": "QQNum:807922095",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:815751507",
                "key": "QQNum",
                "label": "QQNum:815751507",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:819579741",
                "key": "QQNum",
                "label": "QQNum:819579741",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:823860591",
                "key": "QQNum",
                "label": "QQNum:823860591",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:83663647",
                "key": "QQNum",
                "label": "QQNum:83663647",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:857066092",
                "key": "QQNum",
                "label": "QQNum:857066092",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:900000",
                "key": "QQNum",
                "label": "QQNum:900000",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:10000000",
                "key": "QQNum",
                "label": "QQNum:10000000",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:100001",
                "key": "QQNum",
                "label": "QQNum:100001",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:10271",
                "key": "QQNum",
                "label": "QQNum:10271",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:10817",
                "key": "QQNum",
                "label": "QQNum:10817",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:10916",
                "key": "QQNum",
                "label": "QQNum:10916",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:10927",
                "key": "QQNum",
                "label": "QQNum:10927",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:10937",
                "key": "QQNum",
                "label": "QQNum:10937",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:11110",
                "key": "QQNum",
                "label": "QQNum:11110",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:11114",
                "key": "QQNum",
                "label": "QQNum:11114",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:11213",
                "key": "QQNum",
                "label": "QQNum:11213",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:11999",
                "key": "QQNum",
                "label": "QQNum:11999",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:1234567",
                "key": "QQNum",
                "label": "QQNum:1234567",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:14444",
                "key": "QQNum",
                "label": "QQNum:14444",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:21111",
                "key": "QQNum",
                "label": "QQNum:21111",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:22221",
                "key": "QQNum",
                "label": "QQNum:22221",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:22224",
                "key": "QQNum",
                "label": "QQNum:22224",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:22225",
                "key": "QQNum",
                "label": "QQNum:22225",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:30303030",
                "key": "QQNum",
                "label": "QQNum:30303030",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:33331",
                "key": "QQNum",
                "label": "QQNum:33331",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:33332",
                "key": "QQNum",
                "label": "QQNum:33332",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:33334",
                "key": "QQNum",
                "label": "QQNum:33334",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:33335",
                "key": "QQNum",
                "label": "QQNum:33335",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:33336",
                "key": "QQNum",
                "label": "QQNum:33336",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:33337",
                "key": "QQNum",
                "label": "QQNum:33337",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:33338",
                "key": "QQNum",
                "label": "QQNum:33338",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:37777",
                "key": "QQNum",
                "label": "QQNum:37777",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:43210",
                "key": "QQNum",
                "label": "QQNum:43210",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:44000",
                "key": "QQNum",
                "label": "QQNum:44000",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:44440",
                "key": "QQNum",
                "label": "QQNum:44440",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:44441",
                "key": "QQNum",
                "label": "QQNum:44441",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:444444",
                "key": "QQNum",
                "label": "QQNum:444444",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:44445",
                "key": "QQNum",
                "label": "QQNum:44445",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:44446",
                "key": "QQNum",
                "label": "QQNum:44446",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:44447",
                "key": "QQNum",
                "label": "QQNum:44447",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:44448",
                "key": "QQNum",
                "label": "QQNum:44448",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:45555",
                "key": "QQNum",
                "label": "QQNum:45555",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:49999",
                "key": "QQNum",
                "label": "QQNum:49999",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:51111",
                "key": "QQNum",
                "label": "QQNum:51111",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:54444",
                "key": "QQNum",
                "label": "QQNum:54444",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:55551",
                "key": "QQNum",
                "label": "QQNum:55551",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:55552",
                "key": "QQNum",
                "label": "QQNum:55552",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:55554",
                "key": "QQNum",
                "label": "QQNum:55554",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:555555",
                "key": "QQNum",
                "label": "QQNum:555555",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:55556",
                "key": "QQNum",
                "label": "QQNum:55556",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:55557",
                "key": "QQNum",
                "label": "QQNum:55557",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:55588",
                "key": "QQNum",
                "label": "QQNum:55588",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:619951999",
                "key": "QQNum",
                "label": "QQNum:619951999",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:62222",
                "key": "QQNum",
                "label": "QQNum:62222",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:64444",
                "key": "QQNum",
                "label": "QQNum:64444",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:65432",
                "key": "QQNum",
                "label": "QQNum:65432",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:66661",
                "key": "QQNum",
                "label": "QQNum:66661",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:66663",
                "key": "QQNum",
                "label": "QQNum:66663",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:66667",
                "key": "QQNum",
                "label": "QQNum:66667",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:66669",
                "key": "QQNum",
                "label": "QQNum:66669",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:67777",
                "key": "QQNum",
                "label": "QQNum:67777",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:71111",
                "key": "QQNum",
                "label": "QQNum:71111",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:72222",
                "key": "QQNum",
                "label": "QQNum:72222",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:73333",
                "key": "QQNum",
                "label": "QQNum:73333",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:74444",
                "key": "QQNum",
                "label": "QQNum:74444",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:77770",
                "key": "QQNum",
                "label": "QQNum:77770",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:77771",
                "key": "QQNum",
                "label": "QQNum:77771",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:77772",
                "key": "QQNum",
                "label": "QQNum:77772",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:77773",
                "key": "QQNum",
                "label": "QQNum:77773",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:77775",
                "key": "QQNum",
                "label": "QQNum:77775",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:77776",
                "key": "QQNum",
                "label": "QQNum:77776",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:77778",
                "key": "QQNum",
                "label": "QQNum:77778",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:77779",
                "key": "QQNum",
                "label": "QQNum:77779",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:78888",
                "key": "QQNum",
                "label": "QQNum:78888",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:81111",
                "key": "QQNum",
                "label": "QQNum:81111",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:82222",
                "key": "QQNum",
                "label": "QQNum:82222",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:83333",
                "key": "QQNum",
                "label": "QQNum:83333",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:84444",
                "key": "QQNum",
                "label": "QQNum:84444",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:85630",
                "key": "QQNum",
                "label": "QQNum:85630",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:88788",
                "key": "QQNum",
                "label": "QQNum:88788",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:88800",
                "key": "QQNum",
                "label": "QQNum:88800",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:88884",
                "key": "QQNum",
                "label": "QQNum:88884",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:88885",
                "key": "QQNum",
                "label": "QQNum:88885",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:88887",
                "key": "QQNum",
                "label": "QQNum:88887",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:92222",
                "key": "QQNum",
                "label": "QQNum:92222",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:99000",
                "key": "QQNum",
                "label": "QQNum:99000",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:10671",
                "key": "QQNum",
                "label": "QQNum:10671",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:11515151",
                "key": "QQNum",
                "label": "QQNum:11515151",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:188889851",
                "key": "QQNum",
                "label": "QQNum:188889851",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:28985",
                "key": "QQNum",
                "label": "QQNum:28985",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:2898555",
                "key": "QQNum",
                "label": "QQNum:2898555",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:289855555",
                "key": "QQNum",
                "label": "QQNum:289855555",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:2898588",
                "key": "QQNum",
                "label": "QQNum:2898588",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:28991",
                "key": "QQNum",
                "label": "QQNum:28991",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:28997",
                "key": "QQNum",
                "label": "QQNum:28997",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:28999",
                "key": "QQNum",
                "label": "QQNum:28999",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:33133",
                "key": "QQNum",
                "label": "QQNum:33133",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:4444344",
                "key": "QQNum",
                "label": "QQNum:4444344",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:52033991",
                "key": "QQNum",
                "label": "QQNum:52033991",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:58686",
                "key": "QQNum",
                "label": "QQNum:58686",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:62000",
                "key": "QQNum",
                "label": "QQNum:62000",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:68686",
                "key": "QQNum",
                "label": "QQNum:68686",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            },
            {
                "id": "QQNum:82000",
                "key": "QQNum",
                "label": "QQNum:82000",
                "labelCfg": {
                    "positions": "center"
                },
                "style": {
                    "fill": "#18ffff",
                    "opacity": [
                        0.8
                    ]
                },
                "type": "circle",
                "value": "100000"
            }
        ]
    }
},
                resu: {
                    "code": 200,
                    "msg": "successful!",
                    "result_data": {
                        "edges": [
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1002952878",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1003328825",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:100870277",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:100993029",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1012813603",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1020595837",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1028290420",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1034313020",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1052866439",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1056497303",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1070777877",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1091525868",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1106352597",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1126644390",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:119738209",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1223301247",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1223594149",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1227110866",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:1275664688",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:151699058",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:155123456",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:157897579",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:214514728",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:214557388",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:245787407",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:249699594",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:273182875",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:276888822",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:27801179",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:278345729",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:279174652",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:282354194",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:283945509",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:291127695",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:295662820",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:295855778",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:304018401",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:324027281",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:32436937",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:326671234",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:335332031",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:337009314",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:344272681",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:365790091",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:36742681",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:372780276",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:378833545",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:389923353",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:405823074",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:415801451",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:41770263",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:425754696",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:439942774",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:444308881",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:444759600",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:445790378",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:450456162",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:452476598",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:465167831",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:471137730",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:47329930",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:476844626",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:48334416",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:491668258",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:511473641",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:516444499",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:545645333",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:550208176",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:55240234",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:554761845",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:554784729",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:563394705",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:5791468",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:591218144",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:592284645",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:598581491",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:598949999",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:644027865",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:652314798",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:652431455",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:67276735",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:675092908",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:690120488",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:7175795",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:741191111",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:747094762",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:760982201",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:761547366",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:7682286",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:768739943",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:771524992",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:775235",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:779198705",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:78394047",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:784667622",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:786605416",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:792641245",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:80900443",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:821895170",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:828469",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:837896456",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:837963942",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:838230586",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:839191409",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:840102744",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:846664611",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:847363701",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:849498751",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:85813595",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:859585121",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:861941614",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:865361731",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:865660411",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:86790757",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:870749600",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:876379575",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:897112789",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:917312811",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:923692468",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:924572006",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:931400989",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:931752645",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:931948223",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:932999801",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:936457624",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:940680151",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:947493392",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:947770956",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:964867490",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:97004118",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:973874799",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:995505667",
                                "value": 1
                            },
                            {
                                "source": "QunNum:1000000",
                                "target": "QQNum:996405699",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1002952878",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1002952878",
                                "target": "QunNum:90026323",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1003328825",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:100870277",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:100993029",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:100993029",
                                "target": "QunNum:20025244",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1012813603",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1020595837",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1028290420",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1034313020",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1052866439",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1056497303",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1070777877",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1091525868",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1106352597",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1126644390",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:119738209",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1223301247",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1223594149",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1227110866",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:1275664688",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:151699058",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:151699058",
                                "target": "QunNum:40076269",
                                "value": 1
                            },
                            {
                                "source": "QQNum:151699058",
                                "target": "QunNum:918222",
                                "value": 1
                            },
                            {
                                "source": "QQNum:155123456",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:157897579",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:214514728",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:214557388",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:245787407",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:249699594",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:273182875",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:273182875",
                                "target": "QunNum:40094763",
                                "value": 1
                            },
                            {
                                "source": "QQNum:276888822",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:276888822",
                                "target": "QunNum:90018849",
                                "value": 1
                            },
                            {
                                "source": "QQNum:27801179",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:278345729",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:279174652",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:282354194",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:283945509",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:283945509",
                                "target": "QunNum:90026323",
                                "value": 1
                            },
                            {
                                "source": "QQNum:291127695",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:295662820",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:295662820",
                                "target": "QunNum:50050602",
                                "value": 1
                            },
                            {
                                "source": "QQNum:295855778",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:304018401",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:304018401",
                                "target": "QunNum:70080297",
                                "value": 1
                            },
                            {
                                "source": "QQNum:324027281",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:32436937",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:326671234",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:335332031",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:337009314",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:344272681",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:344272681",
                                "target": "QunNum:10006937",
                                "value": 1
                            },
                            {
                                "source": "QQNum:365790091",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:36742681",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:372780276",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:378833545",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:389923353",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:405823074",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:415801451",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:41770263",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:425754696",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:439942774",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:444308881",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:444759600",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:445790378",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:445790378",
                                "target": "QunNum:50033507",
                                "value": 1
                            },
                            {
                                "source": "QQNum:445790378",
                                "target": "QunNum:50055180",
                                "value": 1
                            },
                            {
                                "source": "QQNum:445790378",
                                "target": "QunNum:50055304",
                                "value": 1
                            },
                            {
                                "source": "QQNum:445790378",
                                "target": "QunNum:50077580",
                                "value": 1
                            },
                            {
                                "source": "QQNum:450456162",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:452476598",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:465167831",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:465167831",
                                "target": "QunNum:20080824",
                                "value": 1
                            },
                            {
                                "source": "QQNum:471137730",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:47329930",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:476844626",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:48334416",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:491668258",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:511473641",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:516444499",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:545645333",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:550208176",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:55240234",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:554761845",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:554784729",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:563394705",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:5791468",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:5791468",
                                "target": "QunNum:80064405",
                                "value": 1
                            },
                            {
                                "source": "QQNum:591218144",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:592284645",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:598581491",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:598949999",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:644027865",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:644027865",
                                "target": "QunNum:30065366",
                                "value": 1
                            },
                            {
                                "source": "QQNum:652314798",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:652314798",
                                "target": "QunNum:10021905",
                                "value": 1
                            },
                            {
                                "source": "QQNum:652431455",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:652431455",
                                "target": "QunNum:50033507",
                                "value": 1
                            },
                            {
                                "source": "QQNum:652431455",
                                "target": "QunNum:50055180",
                                "value": 1
                            },
                            {
                                "source": "QQNum:652431455",
                                "target": "QunNum:50055304",
                                "value": 1
                            },
                            {
                                "source": "QQNum:652431455",
                                "target": "QunNum:50055372",
                                "value": 1
                            },
                            {
                                "source": "QQNum:652431455",
                                "target": "QunNum:50077580",
                                "value": 1
                            },
                            {
                                "source": "QQNum:652431455",
                                "target": "QunNum:50099123",
                                "value": 1
                            },
                            {
                                "source": "QQNum:67276735",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:675092908",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:690120488",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:7175795",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:741191111",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:747094762",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:760982201",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:761547366",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:7682286",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:768739943",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:771524992",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:775235",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:775235",
                                "target": "QunNum:20071264",
                                "value": 1
                            },
                            {
                                "source": "QQNum:779198705",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:78394047",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:784667622",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:786605416",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:792641245",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:80900443",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:80900443",
                                "target": "QunNum:20030003",
                                "value": 1
                            },
                            {
                                "source": "QQNum:80900443",
                                "target": "QunNum:981091",
                                "value": 1
                            },
                            {
                                "source": "QQNum:821895170",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:828469",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:837896456",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:837963942",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:838230586",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:839191409",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:840102744",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:846664611",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:847363701",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:849498751",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:85813595",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:859585121",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:861941614",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:865361731",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:865660411",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:865660411",
                                "target": "QunNum:70095060",
                                "value": 1
                            },
                            {
                                "source": "QQNum:86790757",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:870749600",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:876379575",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:897112789",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:917312811",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:923692468",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:924572006",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:931400989",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:931752645",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:931948223",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:932999801",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:936457624",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:940680151",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:947493392",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:947770956",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:964867490",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:97004118",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:973874799",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:995505667",
                                "target": "QunNum:1000000",
                                "value": 1
                            },
                            {
                                "source": "QQNum:996405699",
                                "target": "QunNum:1000000",
                                "value": 1
                            }
                        ],
                        "nodes": [
                            {
                                "id": "QunNum:1000000",
                                "key": "QunNum",
                                "label": "QunNum:1000000",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1002952878",
                                "key": "QunNum",
                                "label": "QQNum:1002952878",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1003328825",
                                "key": "QunNum",
                                "label": "QQNum:1003328825",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:100870277",
                                "key": "QunNum",
                                "label": "QQNum:100870277",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:100993029",
                                "key": "QunNum",
                                "label": "QQNum:100993029",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1012813603",
                                "key": "QunNum",
                                "label": "QQNum:1012813603",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1020595837",
                                "key": "QunNum",
                                "label": "QQNum:1020595837",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1028290420",
                                "key": "QunNum",
                                "label": "QQNum:1028290420",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1034313020",
                                "key": "QunNum",
                                "label": "QQNum:1034313020",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1052866439",
                                "key": "QunNum",
                                "label": "QQNum:1052866439",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1056497303",
                                "key": "QunNum",
                                "label": "QQNum:1056497303",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1070777877",
                                "key": "QunNum",
                                "label": "QQNum:1070777877",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1091525868",
                                "key": "QunNum",
                                "label": "QQNum:1091525868",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1106352597",
                                "key": "QunNum",
                                "label": "QQNum:1106352597",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1126644390",
                                "key": "QunNum",
                                "label": "QQNum:1126644390",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:119738209",
                                "key": "QunNum",
                                "label": "QQNum:119738209",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1223301247",
                                "key": "QunNum",
                                "label": "QQNum:1223301247",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1223594149",
                                "key": "QunNum",
                                "label": "QQNum:1223594149",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1227110866",
                                "key": "QunNum",
                                "label": "QQNum:1227110866",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:1275664688",
                                "key": "QunNum",
                                "label": "QQNum:1275664688",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:151699058",
                                "key": "QunNum",
                                "label": "QQNum:151699058",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:155123456",
                                "key": "QunNum",
                                "label": "QQNum:155123456",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:157897579",
                                "key": "QunNum",
                                "label": "QQNum:157897579",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:214514728",
                                "key": "QunNum",
                                "label": "QQNum:214514728",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:214557388",
                                "key": "QunNum",
                                "label": "QQNum:214557388",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:245787407",
                                "key": "QunNum",
                                "label": "QQNum:245787407",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:249699594",
                                "key": "QunNum",
                                "label": "QQNum:249699594",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:273182875",
                                "key": "QunNum",
                                "label": "QQNum:273182875",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:276888822",
                                "key": "QunNum",
                                "label": "QQNum:276888822",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:27801179",
                                "key": "QunNum",
                                "label": "QQNum:27801179",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:278345729",
                                "key": "QunNum",
                                "label": "QQNum:278345729",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:279174652",
                                "key": "QunNum",
                                "label": "QQNum:279174652",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:282354194",
                                "key": "QunNum",
                                "label": "QQNum:282354194",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:283945509",
                                "key": "QunNum",
                                "label": "QQNum:283945509",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:291127695",
                                "key": "QunNum",
                                "label": "QQNum:291127695",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:295662820",
                                "key": "QunNum",
                                "label": "QQNum:295662820",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:295855778",
                                "key": "QunNum",
                                "label": "QQNum:295855778",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:304018401",
                                "key": "QunNum",
                                "label": "QQNum:304018401",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:324027281",
                                "key": "QunNum",
                                "label": "QQNum:324027281",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:32436937",
                                "key": "QunNum",
                                "label": "QQNum:32436937",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:326671234",
                                "key": "QunNum",
                                "label": "QQNum:326671234",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:335332031",
                                "key": "QunNum",
                                "label": "QQNum:335332031",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:337009314",
                                "key": "QunNum",
                                "label": "QQNum:337009314",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:344272681",
                                "key": "QunNum",
                                "label": "QQNum:344272681",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:365790091",
                                "key": "QunNum",
                                "label": "QQNum:365790091",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:36742681",
                                "key": "QunNum",
                                "label": "QQNum:36742681",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:372780276",
                                "key": "QunNum",
                                "label": "QQNum:372780276",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:378833545",
                                "key": "QunNum",
                                "label": "QQNum:378833545",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:389923353",
                                "key": "QunNum",
                                "label": "QQNum:389923353",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:405823074",
                                "key": "QunNum",
                                "label": "QQNum:405823074",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:415801451",
                                "key": "QunNum",
                                "label": "QQNum:415801451",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:41770263",
                                "key": "QunNum",
                                "label": "QQNum:41770263",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:425754696",
                                "key": "QunNum",
                                "label": "QQNum:425754696",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:439942774",
                                "key": "QunNum",
                                "label": "QQNum:439942774",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:444308881",
                                "key": "QunNum",
                                "label": "QQNum:444308881",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:444759600",
                                "key": "QunNum",
                                "label": "QQNum:444759600",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:445790378",
                                "key": "QunNum",
                                "label": "QQNum:445790378",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:450456162",
                                "key": "QunNum",
                                "label": "QQNum:450456162",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:452476598",
                                "key": "QunNum",
                                "label": "QQNum:452476598",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:465167831",
                                "key": "QunNum",
                                "label": "QQNum:465167831",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:471137730",
                                "key": "QunNum",
                                "label": "QQNum:471137730",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:47329930",
                                "key": "QunNum",
                                "label": "QQNum:47329930",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:476844626",
                                "key": "QunNum",
                                "label": "QQNum:476844626",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:48334416",
                                "key": "QunNum",
                                "label": "QQNum:48334416",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:491668258",
                                "key": "QunNum",
                                "label": "QQNum:491668258",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:511473641",
                                "key": "QunNum",
                                "label": "QQNum:511473641",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:516444499",
                                "key": "QunNum",
                                "label": "QQNum:516444499",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:545645333",
                                "key": "QunNum",
                                "label": "QQNum:545645333",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:550208176",
                                "key": "QunNum",
                                "label": "QQNum:550208176",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:55240234",
                                "key": "QunNum",
                                "label": "QQNum:55240234",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:554761845",
                                "key": "QunNum",
                                "label": "QQNum:554761845",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:554784729",
                                "key": "QunNum",
                                "label": "QQNum:554784729",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:563394705",
                                "key": "QunNum",
                                "label": "QQNum:563394705",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:5791468",
                                "key": "QunNum",
                                "label": "QQNum:5791468",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:591218144",
                                "key": "QunNum",
                                "label": "QQNum:591218144",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:592284645",
                                "key": "QunNum",
                                "label": "QQNum:592284645",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:598581491",
                                "key": "QunNum",
                                "label": "QQNum:598581491",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:598949999",
                                "key": "QunNum",
                                "label": "QQNum:598949999",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:644027865",
                                "key": "QunNum",
                                "label": "QQNum:644027865",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:652314798",
                                "key": "QunNum",
                                "label": "QQNum:652314798",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:652431455",
                                "key": "QunNum",
                                "label": "QQNum:652431455",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:67276735",
                                "key": "QunNum",
                                "label": "QQNum:67276735",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:675092908",
                                "key": "QunNum",
                                "label": "QQNum:675092908",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:690120488",
                                "key": "QunNum",
                                "label": "QQNum:690120488",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:7175795",
                                "key": "QunNum",
                                "label": "QQNum:7175795",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:741191111",
                                "key": "QunNum",
                                "label": "QQNum:741191111",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:747094762",
                                "key": "QunNum",
                                "label": "QQNum:747094762",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:760982201",
                                "key": "QunNum",
                                "label": "QQNum:760982201",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:761547366",
                                "key": "QunNum",
                                "label": "QQNum:761547366",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:7682286",
                                "key": "QunNum",
                                "label": "QQNum:7682286",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:768739943",
                                "key": "QunNum",
                                "label": "QQNum:768739943",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:771524992",
                                "key": "QunNum",
                                "label": "QQNum:771524992",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:775235",
                                "key": "QunNum",
                                "label": "QQNum:775235",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:779198705",
                                "key": "QunNum",
                                "label": "QQNum:779198705",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:78394047",
                                "key": "QunNum",
                                "label": "QQNum:78394047",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:784667622",
                                "key": "QunNum",
                                "label": "QQNum:784667622",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:786605416",
                                "key": "QunNum",
                                "label": "QQNum:786605416",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:792641245",
                                "key": "QunNum",
                                "label": "QQNum:792641245",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:80900443",
                                "key": "QunNum",
                                "label": "QQNum:80900443",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:821895170",
                                "key": "QunNum",
                                "label": "QQNum:821895170",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:828469",
                                "key": "QunNum",
                                "label": "QQNum:828469",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:837896456",
                                "key": "QunNum",
                                "label": "QQNum:837896456",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:837963942",
                                "key": "QunNum",
                                "label": "QQNum:837963942",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:838230586",
                                "key": "QunNum",
                                "label": "QQNum:838230586",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:839191409",
                                "key": "QunNum",
                                "label": "QQNum:839191409",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:840102744",
                                "key": "QunNum",
                                "label": "QQNum:840102744",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:846664611",
                                "key": "QunNum",
                                "label": "QQNum:846664611",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:847363701",
                                "key": "QunNum",
                                "label": "QQNum:847363701",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:849498751",
                                "key": "QunNum",
                                "label": "QQNum:849498751",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:85813595",
                                "key": "QunNum",
                                "label": "QQNum:85813595",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:859585121",
                                "key": "QunNum",
                                "label": "QQNum:859585121",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:861941614",
                                "key": "QunNum",
                                "label": "QQNum:861941614",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:865361731",
                                "key": "QunNum",
                                "label": "QQNum:865361731",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:865660411",
                                "key": "QunNum",
                                "label": "QQNum:865660411",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:86790757",
                                "key": "QunNum",
                                "label": "QQNum:86790757",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:870749600",
                                "key": "QunNum",
                                "label": "QQNum:870749600",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:876379575",
                                "key": "QunNum",
                                "label": "QQNum:876379575",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:897112789",
                                "key": "QunNum",
                                "label": "QQNum:897112789",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:917312811",
                                "key": "QunNum",
                                "label": "QQNum:917312811",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:923692468",
                                "key": "QunNum",
                                "label": "QQNum:923692468",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:924572006",
                                "key": "QunNum",
                                "label": "QQNum:924572006",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:931400989",
                                "key": "QunNum",
                                "label": "QQNum:931400989",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:931752645",
                                "key": "QunNum",
                                "label": "QQNum:931752645",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:931948223",
                                "key": "QunNum",
                                "label": "QQNum:931948223",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:932999801",
                                "key": "QunNum",
                                "label": "QQNum:932999801",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:936457624",
                                "key": "QunNum",
                                "label": "QQNum:936457624",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:940680151",
                                "key": "QunNum",
                                "label": "QQNum:940680151",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:947493392",
                                "key": "QunNum",
                                "label": "QQNum:947493392",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:947770956",
                                "key": "QunNum",
                                "label": "QQNum:947770956",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:964867490",
                                "key": "QunNum",
                                "label": "QQNum:964867490",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:97004118",
                                "key": "QunNum",
                                "label": "QQNum:97004118",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:973874799",
                                "key": "QunNum",
                                "label": "QQNum:973874799",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:995505667",
                                "key": "QunNum",
                                "label": "QQNum:995505667",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QQNum:996405699",
                                "key": "QunNum",
                                "label": "QQNum:996405699",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "circle",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:90026323",
                                "key": "QunNum",
                                "label": "QunNum:90026323",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:20025244",
                                "key": "QunNum",
                                "label": "QunNum:20025244",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:40076269",
                                "key": "QunNum",
                                "label": "QunNum:40076269",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:918222",
                                "key": "QunNum",
                                "label": "QunNum:918222",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:40094763",
                                "key": "QunNum",
                                "label": "QunNum:40094763",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:90018849",
                                "key": "QunNum",
                                "label": "QunNum:90018849",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:50050602",
                                "key": "QunNum",
                                "label": "QunNum:50050602",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:70080297",
                                "key": "QunNum",
                                "label": "QunNum:70080297",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:10006937",
                                "key": "QunNum",
                                "label": "QunNum:10006937",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:50033507",
                                "key": "QunNum",
                                "label": "QunNum:50033507",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:50055180",
                                "key": "QunNum",
                                "label": "QunNum:50055180",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:50055304",
                                "key": "QunNum",
                                "label": "QunNum:50055304",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:50077580",
                                "key": "QunNum",
                                "label": "QunNum:50077580",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:20080824",
                                "key": "QunNum",
                                "label": "QunNum:20080824",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:80064405",
                                "key": "QunNum",
                                "label": "QunNum:80064405",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:30065366",
                                "key": "QunNum",
                                "label": "QunNum:30065366",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:10021905",
                                "key": "QunNum",
                                "label": "QunNum:10021905",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:50055372",
                                "key": "QunNum",
                                "label": "QunNum:50055372",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:50099123",
                                "key": "QunNum",
                                "label": "QunNum:50099123",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:20071264",
                                "key": "QunNum",
                                "label": "QunNum:20071264",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:20030003",
                                "key": "QunNum",
                                "label": "QunNum:20030003",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:981091",
                                "key": "QunNum",
                                "label": "QunNum:981091",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            },
                            {
                                "id": "QunNum:70095060",
                                "key": "QunNum",
                                "label": "QunNum:70095060",
                                "labelCfg": {
                                    "positions": "center"
                                },
                                "type": "ellipse",
                                "value": "1000000"
                            }
                        ]
                    }
                },
                QQNum: "",
                QunNum: "",
                error: false,
                graph: {},
                data: [
                    {genre: "Sports", sold: 275},
                    {genre: "Strategy", sold: 115},
                    {genre: "Action", sold: 120},
                    {genre: "Shooter", sold: 350},
                    {genre: "Other", sold: 150}
                ]
            };
        }, methods: {
            init() {
                let that = this
                that.leading = true
                that.happy = false
                that.error = false
                that.result.code = 400
            },
            ini() {
                this.resu = this.result
                this.graph.clear()
                const graph = this.graph
                var data = this.result.result_data
                console.log(data)
                const nodes = data.nodes;
                // randomize the node size
                nodes.forEach((node) => {
                    node.size = 15;
                });
                graph.data({
                    nodes,
                    edges: data.edges.map(function (edge, i) {
                        edge.id = 'edge' + i;
                        return Object.assign({}, edge);
                    }),
                });
                graph.render();

                // this.graph.destroy()
                // this.initComponent()
            },
            initComponent() {
                const container = document.getElementById('container');
                const width = container.scrollWidth;
                const height = container.scrollHeight || 500;
                const graph = new G6.Graph({
                    defaultNode: {

                        labelCfg: {
                            // 节点上的标签文本样式配置
                            style: {

                                fontSize: 0,
                            },
                        },
                    },
                    defaultEdge: {
                        style: {
                            opacity: 1.0, // 边透明度
                            stroke: '#ff4757', // 边描边颜色
                        },
                    },
                    container: 'container',
                    width,
                    height,
                    layout: {
                        type: 'force',
                        preventOverlap: true,
                    },
                    modes: {
                        default: [
                            'drag-canvas',
                            {
                                type: 'tooltip', // 提示框
                                formatText(model) {
                                    // console.log(model.label)
                                    // 提示框文本内容
                                    const text = model.label;
                                    return text;
                                },
                            },
                        ],
                    },
                });
                let that = this
                var data = that.resu.result_data
                console.log(data)
                const nodes = data.nodes;
                // randomize the node size
                nodes.forEach((node) => {
                    node.size = 15;
                });
                graph.data({
                    nodes,
                    edges: data.edges.map(function (edge, i) {
                        edge.id = 'edge' + i;
                        return Object.assign({}, edge);
                    }),
                });
                graph.render();

                const forceLayout = graph.get('layoutController').layoutMethod;

                graph.on('node:dragstart', function (e) {
                    graph.layout();
                    refreshDragedNodePosition(e);
                });
                graph.on('node:drag', function (e) {
                    forceLayout.execute();
                    refreshDragedNodePosition(e);
                });
                graph.on('node:dragend', function (e) {
                    e.item.get('model').fx = null;
                    e.item.get('model').fy = null;
                });


                if (typeof window !== 'undefined')
                    window.onresize = () => {
                        if (!graph || graph.get('destroyed')) return;
                        if (!container || !container.scrollWidth || !container.scrollHeight) return;
                        graph.changeSize(container.scrollWidth, container.scrollHeight);
                    };

                function refreshDragedNodePosition(e) {
                    const model = e.item.get('model');
                    model.fx = e.x;
                    model.fy = e.y;
                }
                return graph
            }
        }
    }
    ;
</script>

<style scoped>

</style>