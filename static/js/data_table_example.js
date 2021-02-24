$(document).ready(function($)
	{
		//ajax row data
        var ajax_data = data.dg_records

		//--->convert it into datatable arrays > start
		var data_table_arr = []
		$.each(ajax_data, function(index, val)
		{
			data_table_arr.push([
                val.pid_fyt_pmy_dpt_cd,
                val.pid_fyt_pmy_dpt_dsc_tx,
                val.pid_fyt_rec_dpt_cd,
                val.pid_fyt_rec_dpt_dsc_tx,
                val.pid_fyt_sub_dpt_cd,
                val.pid_fyt_sub_dpt_dsc_tx,
                val.pid_fyt_com_cd,
                val.pid_fyt_com_dsc_tx,
                val.pid_fyt_sub_com_cd,
                val.pid_fyt_sub_com_dsc_tx,
                val.demand_group_code,
                val.demand_group_dsc,

			])

		});
		//--->convert it into datatable arrays > end


 		//id of your datatable you want populate rows for
	    $('#your-tabulator_test').DataTable(
	    {
	    	data: data_table_arr,
	    	"lengthMenu": [ [10,25, 50, 100, -1], [10, 25, 50, 100, "All"] ],
			"pageLength": 25,
	    	columns: [
				{ title: 'pid_fyt_pmy_dpt_cd' },
				{ title: "pid_fyt_pmy_dpt_dsc_tx" },
				{ title: "pid_fyt_rec_dpt_cd" },
				{ title: "pid_fyt_rec_dpt_dsc_tx" },
				{ title: "pid_fyt_sub_dpt_cd" },
				{ title: "pid_fyt_sub_dpt_dsc_tx" },
				{ title: "pid_fyt_com_cd" },
				{ title: "pid_fyt_com_dsc_tx" },
				{ title: "pid_fyt_sub_com_cd" },
				{ title: "pid_fyt_sub_com_dsc_tx" },
				{ title: "demand_group_code" },
				{ title: "demand_group_dsc" },
			],
	    } );
	});
