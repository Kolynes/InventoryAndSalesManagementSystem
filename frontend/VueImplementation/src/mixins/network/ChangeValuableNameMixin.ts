import http from "../../plugins/http";


/**
 * @author Kolynes Chinedu
 */
class ChangeValuableNameMixin {

    /**
     * Default constructor
     */
    constructor() {}

    /**
     * 
     */
    name : String;

    /**
     * 
     */
    serial : String;

    /**
     * 
     */
    changingValuableName : Boolean;

    /**
     * @return
     */
    async changeValuableName() : Promise<Object> {
        this.changingValuableName = true;
        var returnObject : Object = await http.getJSON("/change-valuable-name/", {
            serial: this.serial,
            name: this.name
        }, "POST")
        this.changingValuableName = false;
        return returnObject;
    }

}
export = ChangeValuableNameMixin;