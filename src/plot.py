from plotly.subplots import make_subplots
from plotly import graph_objects as go
from plotly import offline
import numpy as np

def plot_and_export(df=None, df_dlog_all=None, yhat_mean=None, yhat_conf_int_0=None, yhat_conf_int_1=None, yhat_conf_int_2=None, yhat_conf_int_3=None, yhat_conf_int_75_0=None, yhat_conf_int_75_1=None, yhat_conf_int_75_2=None, yhat_conf_int_75_3=None, name_fig="model_output", delai_dernier_jour=0):
    fig = make_subplots(rows=4, 
                        cols=1, 
                        vertical_spacing = 0.1,
                        subplot_titles=("<b>New cases</b>", "<b>Hospital beds</b>", "<b>Intensive Care Unit beds</b>", "<b>Deaths</b>"))

    fig.add_trace(
        go.Scatter(
            x=yhat_conf_int_75_0.index,
            y=10**(np.log10(df["new_cases"].values[-1-delai_dernier_jour]) + yhat_conf_int_75_0["mean_ci_lower"].cumsum()),
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
            y=10**(np.log10(df["new_cases"].values[-1-delai_dernier_jour]) + yhat_conf_int_75_0["mean_ci_upper"].cumsum()),
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
            y=10**(np.log10(df["new_cases"].values[-1-delai_dernier_jour]) + yhat_conf_int_0["mean_ci_lower"].cumsum()),
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
            y=10**(np.log10(df["new_cases"].values[-1-delai_dernier_jour]) + yhat_conf_int_0["mean_ci_upper"].cumsum()),
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
            y=10**(np.log10(df["new_cases"].values[-1-delai_dernier_jour]) + yhat_mean["new_cases"].cumsum()),
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
            y=10**(np.log10(df["new_cases"].values[0]) + df_dlog_all["new_cases"].cumsum()),
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
            y=10**(np.log10(df["hosp"].values[-1-delai_dernier_jour]) + yhat_conf_int_75_1["mean_ci_lower"].cumsum()),
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
            y=10**(np.log10(df["hosp"].values[-1-delai_dernier_jour]) + yhat_conf_int_75_1["mean_ci_upper"].cumsum()),
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
            y=10**(np.log10(df["hosp"].values[-1-delai_dernier_jour]) + yhat_conf_int_1["mean_ci_lower"].cumsum()),
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
            y=10**(np.log10(df["hosp"].values[-1-delai_dernier_jour]) + yhat_conf_int_1["mean_ci_upper"].cumsum()),
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
            y=10**(np.log10(df["hosp"].values[-1-delai_dernier_jour]) + yhat_mean["hosp"].cumsum()),
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
            y=10**(np.log10(df["hosp"].values[0]) + df_dlog_all["hosp"].cumsum()),
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
            y=10**(np.log10(df["rea"].values[-1-delai_dernier_jour]) + yhat_conf_int_75_2["mean_ci_lower"].cumsum()),
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
            y=10**(np.log10(df["rea"].values[-1-delai_dernier_jour]) + yhat_conf_int_75_2["mean_ci_upper"].cumsum()),
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
            y=10**(np.log10(df["rea"].values[-1-delai_dernier_jour]) + yhat_conf_int_2["mean_ci_lower"].cumsum()),
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
            y=10**(np.log10(df["rea"].values[-1-delai_dernier_jour]) + yhat_conf_int_2["mean_ci_upper"].cumsum()),
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
            y=10**(np.log10(df["rea"].values[-1-delai_dernier_jour]) + yhat_mean["rea"].cumsum()),
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
            y=10**(np.log10(df["rea"].values[0]) + df_dlog_all["rea"].cumsum()),
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
            y=10**(np.log10(df["incid_dc"].values[-1-delai_dernier_jour]) + yhat_conf_int_75_3["mean_ci_lower"].cumsum()),
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
            y=10**(np.log10(df["incid_dc"].values[-1-delai_dernier_jour]) + yhat_conf_int_75_3["mean_ci_upper"].cumsum()),
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
            y=10**(np.log10(df["incid_dc"].values[-1-delai_dernier_jour]) + yhat_conf_int_3["mean_ci_lower"].cumsum()),
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
            y=10**(np.log10(df["incid_dc"].values[-1-delai_dernier_jour]) + yhat_conf_int_3["mean_ci_upper"].cumsum()),
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
            y=10**(np.log10(df["incid_dc"].values[-1-delai_dernier_jour]) + yhat_mean["incid_dc"].cumsum()),
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
            y=10**(np.log10(df["incid_dc"].values[0]) + df_dlog_all["incid_dc"].cumsum()),
            marker_color="black",
            mode="lines",
            name="Deaths",
            showlegend=False
        ),
        row=4,
        col=1
    )

    fig.update_xaxes(range=[df_dlog_all.index[-80], yhat_mean.index[-1]])
    fig.update_yaxes(autorange = True)

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
        y=1.1,
        xref="paper",
        yref="paper",
        font=dict(size = 15),
        text=f"Auteurs : @paldama, @GuillaumeRozier.<br>Données : Santé publique France, Ministère de la Santé.<br>Dernière donnée : {df_dlog_all.index.max()} • Dernière projection : {yhat_mean.index.max()}",
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