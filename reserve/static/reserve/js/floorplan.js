// Manually inserted spots coordinates
coordinates = [
  [201, 79],
  [281, 79],
  [218, 177],
  [404, 79],
  [532, 79],
  [416, 174],
  [616, 79],
  [694, 79],
  [771, 79],
  [771, 251],
  [771, 297],
  [289, 267],
  [289, 313],
  [241, 463],
  [293, 463],
  [398, 507],
  [476, 507],
  [553, 507],
];

//////////////////////////////
//// Draw SVG Layer first ////
//////////////////////////////

var firstLayer = project.activeLayer;
firstLayer.name = "firstLayer";

var bgRect2 = new Shape.Rectangle({
  point: [00, 00],
  size: [968, 583],
  strokeColor: "white",
  strokeWidth: 0,
});

// Import SVG
svg = document.getElementById("floorplan");
// console.log("LOADED SVG:: ", svg);

var yourConvertedSVGItem = project.importSVG(svg, {
  expandShapes: true,
  onLoad: function (item) {
    item.bounds = bgRect2.bounds;
    item.sendToBack();
    // console.log(item);
    svg.style.display = "none";
  },
});

// Create group variable and iterate through data with function createCircles to populate
var mygroup = new Group([bgRect2, yourConvertedSVGItem]);

// console.log(mygroup);
for (var i = 0; i < value.length; i++) {
  mygroup.addChild(
    createCircles(value[i], coordinates[i][0], coordinates[i][1])
  );
}

function createCircles(data, x, y) {
  var ws = new Path.Circle({
    center: [x, y],
    radius: 20,
    data: {
      code: data["code"],
      monitors: data["monitors"],
      seats: data["seats"],
      sector: data["sector"],
      status: data["status"],
    },
  });

  // Layout the tooltip above the dot
  var tooltipRect = new Rectangle(
    ws.position + new Point(-50, 15),
    new Size(100, 60)
  );

  // Create tooltip from rectangle
  var tooltip = new Path.Rectangle(tooltipRect, 6);
  tooltip.fillColor = "white";
  tooltip.strokeColor = "black";
  tooltip.name = "tooltip";

  var tooltipText = new PointText({
    content:
      ws.data.code +
      "\n" +
      "Seats: " +
      ws.data.seats +
      "\n" +
      "Monitor: " +
      ws.data.monitors,
    point: tooltip.position + new Point(0, -12),
    fontFamily: "Helvetica",
    fillColor: "black",
    fontWeight: "bold",
    fontSize: 14,
    justification: "center",
  });
  tooltipText.name = "tooltipText";

  // Adds the tooltip and text to the parent (group)
  mygroup.addChild(tooltip);
  mygroup.addChild(tooltipText);
  tooltip.visible = false;
  tooltipText.visible = false;

  if (ws.data.status == "available") {
    ws.fillColor = new Color("rgb(40, 110, 40)");

    ws.onMouseEnter = function (event) {
      ws.fillColor = new Color("rgb(40, 200, 60)");
      tooltip.visible = true;
      tooltipText.visible = true;
      tooltip.bringToFront();
      tooltipText.bringToFront();
    };

    ws.onMouseLeave = function (event) {
      ws.fillColor = new Color("rgb(40, 110, 40)");
      tooltip.visible = false;
      tooltipText.visible = false;
    };

    ws.onClick = function (event) {
      modal_id = "#" + ws.data.code;
      $(modal_id).modal("show");
    };
  } else {
    ws.fillColor = new Color("rgb(190, 0, 40)");
  }

  return ws;
}

function resizeImg() {
  mygroup.fitBounds(view.bounds);
}

view.onFrame = function (event) {
  resizeImg();
};

// console.log(view.bounds);
// project.activeLayer.fitBounds(view.bounds);
