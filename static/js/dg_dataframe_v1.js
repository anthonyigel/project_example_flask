
$(document).ready(function() {
	// Load Data in JS
    //new_dg_data row data
    {% autoescape off %}
    var new_dg_df = {{ new_dg_data | safe}};
    {% endautoescape %}


  //ROOT TABLE
  $('#dg_main_table').bootstrapTable({
      data: new_dg_df,
      detailFormatter: detailFormatter
  });

  var detailTableRowClicked = false;
  function detailFormatter(index, row, element) {
		var expandedRow = row.id;
		$(element).html(
            "<table id='detailTable"+expandedRow+"'>" +
            "<thead>" +
            "<tr>" +
            "<th data-field='id2' data-align='center' data-width='20px'>id2</th>" +
            "<th data-field='stage' data-visible='false'>Stage</th>" +
            "<th data-field='pid_fyt_pmy_dpt_cd' data-visible='false'>Primary Department</th>" +
            "<th data-field='pid_fyt_pmy_dpt_dsc_tx' data-visible='false'>Primary Department Description</th>" +
            "<th data-field='pid_fyt_rec_dpt_cd' data-visible='false'>Recap Department</th>" +
            "<th data-field='pid_fyt_rec_dpt_dsc_tx' data-visible='false'>Recap Department Description</th>" +
            "<th data-field='pid_fyt_sub_dpt_cd' data-visible='false'>Sub-Department</th>" +
            "<th data-field='pid_fyt_sub_dpt_dsc_tx' data-visible='false'>Sub-Department Description</th>" +
            "<th data-field='pid_fyt_com_cd'>Commodity</th>" +
            "<th data-field='pid_fyt_com_dsc_tx'>Commodity Description</th>" +
            "<th data-field='pid_fyt_sub_com_cd' data-visible='false'>Sub-Commodity Code</th>" +
            "<th data-field='pid_fyt_sub_com_dsc_tx' data-visible='false'>Sub-Commodity Description</th>" +
            "<th data-field='demand_group_code' id='dg_code'>Demand Group Code</th>" +
            "<th data-field='demand_group_dsc' id='dg_desc'>Demand Group Description</th>" +
            "</tr>" +
            "</thead>" +
            "</table>");
		$('#dg_unchanged_table'+expandedRow).bootstrapTable({
            data: unchanged_dg_df,
            checkboxHeader: false
		});

    $('#dg_unchanged_table'+expandedRow).on('check.bs.table', function (e, row, $el) {
    	detailTableRowClicked = true;
    	removeConfirmationDialog(expandedRow, row, this.id);
    });
  }

    //NESTED TABLE
    //unchanged_dg_data row data
    {% autoescape off %}
    var unchanged_dg_df = {{ unchanged_dg_data | safe}};
    {% endautoescape %}

  function removeConfirmationDialog(expandedRow, row, caller) {
		$("#dialogRemove").dialog({
			modal: true,
			buttons: [{
					text: "OK",
					click: function() {
							$(this).dialog("close");
						}
				},{
					text: "Cancel",
            click: function() {
              if (caller == "dg_main_table") {
                $('#'+caller).bootstrapTable('uncheck', row.id-1);
              } else if (caller == "dg_unchanged_table"+expandedRow) {
                $('#dg_unchanged_table'+expandedRow).bootstrapTable('uncheck', row.id2-1);
              }
           		$(this).dialog("close");
            }
				}
			],
		});
	}

 //If you want one panel opened at the time then uncomment below
  /*var oldRow = null
  $('#summaryTable').on('expand-row.bs.table', function (index, row, $detail) {
    if (oldRow !== null && oldRow !== row) {$('#summaryTable').bootstrapTable('collapseRow', oldRow);}
    oldRow = row;

  });*/
 	$('#dg_main_table').on('check.bs.table', function (e, row, $el) {
    if (!detailTableRowClicked) {  // <---This condition is to prevent code execution when clicking a checkbox in a nested table. Unfortunately Bootstrap-table recognizes it as if it was also a click in a root table.
        removeConfirmationDialog(null, row, this.id);
    }
  	detailTableRowClicked = false;
  });
});
