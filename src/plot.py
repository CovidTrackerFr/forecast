from plotly.subplots import make_subplots
from plotly import graph_objects as go
from plotly import offline

def plot_and_export(df_dlog_all=None, yhat_mean=None, yhat_conf_int_0=None, yhat_conf_int_1=None, yhat_conf_int_2=None, yhat_conf_int_3=None, yhat_conf_int_75_0=None, yhat_conf_int_75_1=None, yhat_conf_int_75_2=None, yhat_conf_int_75_3=None, name_fig="model_output"):
    fig = make_subplots(rows=4, 
                        cols=1, 
                        vertical_spacing = 0.1,
                        subplot_titles=("<b>New cases</b>", "<b>Hospital beds</b>", "<b>Intensive Care Unit beds</b>", "<b>Deaths</b>"))


    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_75_0.index,
            y=10**yhat_conf_int_75_0["mean_ci_lower"],
            line_width=0,
            mode="lines",
            name="New cases [predicted]",
            showlegend=False
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_75_0.index,
            y=10**yhat_conf_int_75_0["mean_ci_upper"],
            line_width=0,
            fill="tonexty",
            fillcolor="rgba(107, 192, 250, 0.8)",
            mode="lines",
            name="New cases [predicted]",
            showlegend=False
        ),
        row=1,
        col=1
    )


    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_0.index,
            y=10**yhat_conf_int_0["mean_ci_lower"],
            line_width=0,
            mode="lines",
            name="New cases [predicted]",
            showlegend=False
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_0.index,
            y=10**yhat_conf_int_0["mean_ci_upper"],
            line_width=0,
            fill="tonexty",
            fillcolor="rgba(107, 192, 250, 0.4)",
            mode="lines",
            name="New cases [predicted]",
            showlegend=False
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=yhat_mean.index,
            y=10**yhat_mean["new_cases"],
            mode="lines",
            marker=dict(color="rgba(40, 157, 237, 1)"),
            line=dict(dash='dot'),
            name="New cases [predicted]",
            showlegend=False
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df_dlog_all.index,
            y=10**df_dlog_all["new_cases"],
            marker_color="black",
            mode="lines",
            name="New cases",
            showlegend=False
        ),
        row=1,
        col=1
    )

    ###
    #Hosp

    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_75_1.index,
            y=10**yhat_conf_int_75_1["mean_ci_lower"],
            line_width=0,
            mode="lines",
            name="New cases [predicted]",
            showlegend=False
        ),
        row=2,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_75_1.index,
            y=10**yhat_conf_int_75_1["mean_ci_upper"],
            line_width=0,
            fill="tonexty",
            fillcolor="rgba(107, 192, 250, 0.8)",
            mode="lines",
            name="Hospital admissions [predicted]",
            showlegend=False
        ),
        row=2,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_1.index,
            y=10**yhat_conf_int_1["mean_ci_lower"],
            marker_color="blue",
            line_width=0,
            mode="lines",
            name="New cases [predicted]",
            showlegend=False
        ),
        row=2,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_1.index,
            y=10**yhat_conf_int_1["mean_ci_upper"],
            marker_color="blue",
            line_width=0,
            fill="tonexty",
            fillcolor="rgba(107, 192, 250, 0.4)",
            mode="lines",
            name="Hospital admissions [predicted]",
            showlegend=False
        ),
        row=2,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=yhat_mean.index,
            y=10**yhat_mean["hosp"],
            mode="lines",
            marker=dict(color="rgba(40, 157, 237, 1)"),
            line=dict(dash='dot'),
            name="Hospital admissions [predicted]",
            showlegend=False
        ),
        row=2,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df_dlog_all.index,
            y=10**df_dlog_all["hosp"],
            marker_color="black",
            mode="lines",
            name="Hospital admissions",
            showlegend=False
        ),
        row=2,
        col=1
    )

    ###
    # Rea

    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_75_2.index,
            y=10**yhat_conf_int_75_2["mean_ci_lower"],
            line_width=0,
            mode="lines",
            name="ICU admissions [predicted]",
            showlegend=False
        ),
        row=3,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_75_2.index,
            y=10**yhat_conf_int_75_2["mean_ci_upper"],
            line_width=0,
            fill="tonexty",
            fillcolor="rgba(107, 192, 250, 0.8)",
            mode="lines",
            name="ICU admissions [predicted]",
            showlegend=False
        ),
        row=3,
        col=1
    )


    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_2.index,
            y=10**yhat_conf_int_2["mean_ci_lower"],
            line_width=0,
            mode="lines",
            name="ICU admissions [predicted]",
            showlegend=False
        ),
        row=3,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_2.index,
            y=10**yhat_conf_int_2["mean_ci_upper"],
            line_width=0,
            fill="tonexty",
            fillcolor="rgba(107, 192, 250, 0.4)",
            mode="lines",
            name="ICU admissions [predicted]",
            showlegend=False
        ),
        row=3,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=yhat_mean.index,
            y=10**yhat_mean["rea"],
            marker=dict(color="rgba(40, 157, 237, 1)"),
            line=dict(dash='dot'),
            mode="lines",
            name="ICU admissions [predicted]",
            showlegend=False
        ),
        row=3,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df_dlog_all.index,
            y=10**df_dlog_all["rea"],
            marker_color="black",
            mode="lines",
            name="ICU admissions",
            showlegend=False
        ),
        row=3,
        col=1
    )

    ###
    #Deaths
    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_75_3.index,
            y=10**yhat_conf_int_75_3["mean_ci_lower"],
            line_width=0,
            mode="lines",
            name="Deaths [predicted]",
            showlegend=False
        ),
        row=4,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_75_3.index,
            y=10**yhat_conf_int_75_3["mean_ci_upper"],
            line_width=0,
            fill="tonexty",
            fillcolor="rgba(107, 192, 250, 0.8)",
            mode="lines",
            name="Deaths [predicted]",
            showlegend=False
        ),
        row=4,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_3.index,
            y=10**yhat_conf_int_3["mean_ci_lower"],
            line_width=0,
            mode="lines",
            name="Deaths [predicted]",
            showlegend=False
        ),
        row=4,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_3.index,
            y=10**yhat_conf_int_3["mean_ci_upper"],
            line_width=0,
            fill="tonexty",
            fillcolor="rgba(107, 192, 250, 0.4)",
            mode="lines",
            name="Deaths [predicted]",
            showlegend=False
        ),
        row=4,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=yhat_mean.index,
            y=10**yhat_mean["incid_dc"],
            marker=dict(color="rgba(40, 157, 237, 1)"),
            line=dict(dash='dot'),
            mode="lines",
            name="Deaths [predicted]",
            showlegend=False
        ),
        row=4,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df_dlog_all.index,
            y=10**df_dlog_all["incid_dc"],
            marker_color="black",
            mode="lines",
            name="Deaths",
            showlegend=False
        ),
        row=4,
        col=1
    )

    fig.update_xaxes(range=[df_dlog_all.index[-80], yhat_mean.index[-1]])
    fig.update_yaxes(autorange = True, fixedrange= False)

    fig.add_annotation(
        x=0.5,
        y=-0.15,
        xref="paper",
        yref="paper",
        font=dict(family="Courier New, monospace"),
        text="Model VARX(p=14). Endog variables: dlog(new_cases), dlog(hosp_adm), dlog(ICU_adm), dlog(deaths).<br>Exog variable : dlog(booster_sum). All variable are smoothed (rolling 7 days mean).<br>Confidence intervals 97%/75%.",
        showarrow=False
    )

    fig.add_annotation(
        x=0.5,
        y=1.15,
        xref="paper",
        yref="paper",
        font=dict(size = 25),
        text="<b>EpiVAR</b> France Covid Forecast using VARX model",
        showarrow=False
    )

    fig.add_annotation(
        x=0.5,
        y=1.08,
        xref="paper",
        yref="paper",
        font=dict(size = 15),
        text="Authors : @paldama, @GuillaumeRozier.<br>Data : Santé publique France, Ministère de la Santé.",
        showarrow=False   
    )

    fig.update_layout(
        xaxis=dict(nticks=25),
        xaxis2=dict(nticks=25),
        xaxis3=dict(nticks=25),
        xaxis4=dict(nticks=25),

        yaxis=dict(
            side="right",
            nticks=10,
            titlefont=dict(
                color="#1f77b4"
            ),
            tickfont=dict(
                color="#1f77b4"
            )
        ),
        yaxis2=dict(
            side="right",
            nticks=10,
            titlefont=dict(
                color="#1f77b4"
            ),
            tickfont=dict(
                color="#1f77b4"
            )
        ),
        yaxis3=dict(
            side="right",
            nticks=10,
            titlefont=dict(
                color="#1f77b4"
            ),
            tickfont=dict(
                color="#1f77b4"
            )
        ),
        yaxis4=dict(
            side="right",
            nticks=10,
            titlefont=dict(
                color="#1f77b4"
            ),
            tickfont=dict(
                color="#1f77b4"
            )
        ),
        margin=dict(
            t = 150,
            b = 150
        )
    )


    fig.write_image(f"output/{name_fig}.png", engine="kaleido", width=700, height=1100, scale=2)
    offline.plot(fig, filename = f"output/{name_fig}.html", auto_open=False)
    #fig.show()