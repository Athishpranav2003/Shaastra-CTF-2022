const express = require("express")
const app = express()
const jwt = require("jsonwebtoken")
const fs = require("fs")
var cookieParser = require('cookie-parser')

function between(min, max) {
    return Math.floor(
        Math.random() * (max - min + 1) + min
    )
}

app.use(cookieParser())

function check_jwt(tok) {
    let key = fs.readFileSync("./key");
    let algo = "";
    let head;
    let body;
    try {
        let b = new Buffer(tok.split(".")[0], 'base64');
        b = b.toString('ascii');
        let c = new Buffer(tok.split(".")[1], 'base64');
        c = c.toString('ascii');
        head = JSON.parse(b);
        body = JSON.parse(c)
        console.log(b, c);
    } catch (e) {
        return false;
    }
    if (head["alg"] == "none" || head["alg"] == undefined) {

        if (body["id"] == "0") return true;
        else return false;
    }
    else {
        try {
            let t = jwt.verify(tok, key);
            if (t["id"] == "0") {
                return true
            }
            else { return false; }
        } catch (error) {
            return false
        }
    }
}
app.get("/", (req, res) => {
    let key = fs.readFileSync("./key")

    if (req.cookies["jwt"] && check_jwt(req.cookies["jwt"])) {
        res.send("<h1> ShaastraCTF{jwt_can_be_made_m0re_5ecure} </h1>")
    }
    else {
        const uid = between(5, 50)
        const tok = jwt.sign({
            id: uid
        }, key)
        res.cookie("jwt", tok);
        res.send("<h1>  You cannot see the flag  </h1>");
    }
})

app.get("/read_jwt", (req, res) => {
    let tok = req.cookies["jwt"];
    console.log(tok)

})

app.listen(3000, () => console.log("listening"))
