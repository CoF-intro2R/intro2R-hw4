# CoF-Intro2R Homework 4

In this homework, we will continue working with the HJ Andrews vertebrate data. The data are stored in the `Data/` directory in your GitHub repo. You will practice some more data wrangling as well as plotting using package `ggplot2`. You will also get a peak into how your code can be *modular*. That is, your scripts don't have to stand alone. They can be referenced in other scripts. This is ultimately how R packages work. There is a script for each function in the package, which can then be referenced and the code in the function script run in other analysis scripts without needing to rewrite the code. This is the key to avoiding R scripts with thousands to tens of thousands of lines. If something goes wrong in a humongous script, it can be difficult to diagnose, but if the script is made up of smaller, modular components, it is less daunting to check one module at a time and easier to pinpoint the line that is causing the problem.

# Instructions

1.  As has been the usual practice so far in the course, create a directory called `R` in your homework directory. Additionally, create a directory called `Figures`.

2.  Copy your R script `hw3.R` from homework 3 into the R directory and rename it `data_cleaning.R`.

    i.  Comment out the lines of this script used to save the final dataset to a csv file.

    ii. Add the following lines, replacing the arguments with the names you gave to the different datasets when you initially loaded them into memory. For example, I assigned the trout data the name `trout` when I loaded the data, so I would replace `<trout_data>` with `trout`.

``` r
rm(<coordinate_data>, <salamander_data>, <trout_data>)
```

3.  Save this script and create a new R script called `R/hw4.R`. At the top of `hw4.R`, load the `tidyverse` library and then add the line

``` r
source(here::here("R/data_cleaning.R"))
```

4.  Run the line above. What happened?

5.  Create a summary dataset that includes the number of individuals of each species captured in each year as well as the average mass of the individuals caught in each year. *Hint: `dplyr::group_by()` and `dplyr::summarise()` will be your friends for this.*

6.  Create a figure that shows the number of each species caught over time. Customize your figure (Do not just use the default settings!), and make sure to make all your labels clear and publication worthy.

7.  Create a figure that shows the average mass of individuals caught over time for each species. Again, shoot for a publication-worthy graphic.

8.  Save your figures using `ggsave()`. Name the figure of counts `Figures/num_captures_hja_verts.png` and the figure of mean mass `Figures/mean_mass_hja_verts.png`.
