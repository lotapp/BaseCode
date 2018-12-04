let show = async (urls) => {
    for (const url of urls) {
        let data = await $.ajax({ url: url, dataType: "json" });
        console.log(data);
    }
    return "ok";
}

let test = async () => {
    let result = await show(["./data/user.json", "./data/list.txt", "./data/package.json"]);
    return result;
}