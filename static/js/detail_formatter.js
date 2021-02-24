<!--- Detail View of second table -->
    function detailFormatter(index, row, element) {


        var target_comm_cd = row.pid_fyt_com_cd

        var html = []
            $.each(row, function (key, value) {

                $(element).html($('#dg_unchanged_table').clone(true).attr('id', "tbl_" + row.id).show());
            });

    }
