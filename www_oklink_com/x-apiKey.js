window = {
    btoa(data){
        return btoa(data);
    }
}

function o(t, e) {
    for (var r = 0; r < e.length; r++) {
        var n = e[r];
        n.enumerable = n.enumerable || !1,
            n.configurable = !0,
        "value" in n && (n.writable = !0),
            Object.defineProperty(t, n.key, n)
    }
}

var i = new (function () {
    function t() {
        !function (t, e) {
            if (!(t instanceof e))
                throw new TypeError("Cannot call a class as a function")
        }(this, t),
            this.API_KEY = "a2c903cc-b31e-4547-9299-b6d07b7631ab"
    }

    var e, r;
    return e = t,
    (r = [{
        key: "encryptApiKey",
        value: function () {
            var t = this.API_KEY
                , e = t.split("")
                , r = e.splice(0, 8);
            return e.concat(r).join("")
        }
    }, {
        key: "encryptTime",
        value: function (t) {
            var e = (1 * t + 1111111111111).toString().split("")
                , r = parseInt(10 * Math.random(), 10)
                , n = parseInt(10 * Math.random(), 10)
                , o = parseInt(10 * Math.random(), 10);
            return e.concat([r, n, o]).join("")
        }
    }, {
        key: "comb",
        value: function (t, e) {
            var r = "".concat(t, "|").concat(e);
            return window.btoa(r)
        }
    }, {
        key: "getApiKey",
        value: function () {
            var t = (new Date).getTime()
                , e = this.encryptApiKey();
            return t = this.encryptTime(t),
                this.comb(e, t)
        }
    }]) && o(e.prototype, r),
        Object.defineProperty(e, "prototype", {
            writable: !1
        }),
        t
}());

function white(){
    return i.getApiKey()
}
// console.log(white());

