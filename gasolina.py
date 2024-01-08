{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KJqp9AANOCtf"
      },
      "source": [
        "<img src=\"https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/media/logo/newebac_logo_black_half.png\" alt=\"ebac-logo\">\n",
        "\n",
        "---\n",
        "\n",
        "# **Módulo** | Análise de Dados: Controle de Versão III\n",
        "Caderno de **Exercícios**<br>\n",
        "Professor [André Perez](https://www.linkedin.com/in/andremarcosperez/)\n",
        "\n",
        "---"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "d9jDtUbDOE1-"
      },
      "source": [
        "# **Tópicos**\n",
        "\n",
        "<ol type=\"1\">\n",
        "  <li>Sistema de branchs;</li>\n",
        "  <li>Trabalhando com branchs;</li>\n",
        "  <li>Mover código entre branchs.</li>\n",
        "</ol>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SmoHgt-lwkpD"
      },
      "source": [
        "---"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GABI6OW8OfQ2"
      },
      "source": [
        "# **Exercícios**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kzRDceCvkFj2"
      },
      "source": [
        "## 1\\. Setup"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WCQi-s0Hpd5V"
      },
      "source": [
        "Para realizar os exercicios vamos configurar o `git` e trazer o projeto do GitHub para a a máquina virtual do Google Colab (ou na sua máquina local, as instruções são as mesmas). Para tanto, replique as atividades expostas na aula 1 deste módulo."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HrTLgE0tki6P"
      },
      "source": [
        "### **1.1. Autenticação**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7tIjNOs8q6aZ"
      },
      "source": [
        "Nesta etapa, vamos configura o `git` com suas credenciais."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IwTTh4VKkdKN"
      },
      "source": [
        "import os\n",
        "\n",
        "username = \"KamilaFidelix\" # insira o seu nome de usuário do git\n",
        "os.environ[\"GITHUB_USER\"] = username\n",
        "\n",
        "!git config --global user.name \"${GITHUB_USER}\""
      ],
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8gt4Y28skdKO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1e217323-94a0-463d-a952-ca8e09c6cccc"
      },
      "source": [
        "import os\n",
        "from getpass import getpass\n",
        "\n",
        "usermail = getpass()\n",
        "os.environ[\"GITHUB_MAIL\"] = usermail\n",
        "\n",
        "!git config --global user.email \"${GITHUB_MAIL}\""
      ],
      "execution_count": 27,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "··········\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "BS6vMNnCkdKO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9a0a5bcf-a793-4b60-b61f-784837b5c1a7"
      },
      "source": [
        "import os\n",
        "from getpass import getpass\n",
        "\n",
        "usertoken = getpass()\n",
        "os.environ[\"GITHUB_TOKEN\"] = usertoken"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "··········\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TTh7w8rgkznY"
      },
      "source": [
        "### **1.2. Projeto**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "clBerimQs2PY"
      },
      "source": [
        "Nesta etapa, vamos trazer o projeto do GitHub para máquina local."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fohdVuLzkdKP",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "7188c706-1aa7-42ab-bbd0-43d498fcefe2"
      },
      "source": [
        "!git clone https://github.com/KamilaFidelix/daebacgasolina2.git # insira o link do seu repositório remoto"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'daebacgasolina2'...\n",
            "remote: Enumerating objects: 3, done.\u001b[K\n",
            "remote: Counting objects: 100% (3/3), done.\u001b[K\n",
            "remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0\u001b[K\n",
            "Receiving objects: 100% (3/3), done.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cd /content/daebacgasolina2/"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XicW8NMHksw2",
        "outputId": "e844eaab-99c1-4d10-e9e2-ab878a97641e"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/daebacgasolina2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git add gasolina.csv"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-A_S1dEfoJZr",
        "outputId": "83ce1180-1bb7-4231-b076-d52ce2c260a2"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: pathspec 'gasolina.csv' did not match any files\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git commit -m \"Arquivo gasolina.csv\""
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RRwbtZpboS0U",
        "outputId": "7f92376b-b6c2-46f3-af88-9320979ecde0"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[master (root-commit) 83185ae] Arquivo gasolina.csv\n",
            " 1 file changed, 11 insertions(+)\n",
            " create mode 100644 gasolina.csv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git push origin main"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Sj9BXIk6os6s",
        "outputId": "5684bb0f-285b-4228-f26b-206b77a6993b"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: could not read Username for 'https://github.com': No such device or address\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "waxn4B2UDHyl"
      },
      "source": [
        "---"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "finLQoyyGVmk"
      },
      "source": [
        "## 2\\. Preço da gasolina"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7dJne-O92n2v"
      },
      "source": [
        "O código abaixo gera um arquivo com o preço médio de venda da gasolina na cidade de São Paulo nos 10 primeiros dias de Julho de 2021."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "O_uRYGzqy8OV"
      },
      "source": [
        "> **Nota**: Este arquivo é o mesmo do exercício do módulo anterior."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Uhvy1LG31n1A",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "30b813b1-c867-4175-8c8d-5cfee58e92c2"
      },
      "source": [
        "%%writefile gasolina.csv\n",
        "dia,venda\n",
        "1,5.11\n",
        "2,4.99\n",
        "3,5.02\n",
        "4,5.21\n",
        "5,5.07\n",
        "6,5.09\n",
        "7,5.13\n",
        "8,5.12\n",
        "9,4.94\n",
        "10,5.03"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing gasolina.csv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_gasolina = pd.read_csv('gasolina.csv')"
      ],
      "metadata": {
        "id": "IusbnpXVr4nk"
      },
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lcNhd195zE3t"
      },
      "source": [
        "### **2.1. Branch**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vK0ZbC9ozG4m"
      },
      "source": [
        "Crie uma branch chamada `develop` e aponte o context do `git` para a nova branch. Vamos simular uma atualização no exercício do módulo anterior."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Hz6irIJszysS",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0ef90edf-9fdb-4923-a26f-6b96794a8686"
      },
      "source": [
        "# código de criação da branch develop\n",
        "!git branch develop\n"
      ],
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: A branch named 'develop' already exists.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git checkout develop"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X3gDO8aJqEjN",
        "outputId": "b348074d-af90-4151-df43-f1737af04bdc"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Switched to branch 'develop'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git branch"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j9fQ9OocpoRv",
        "outputId": "19454707-cbaa-431c-9e76-2394fe91dc27"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "* \u001b[32mdevelop\u001b[m\n",
            "  main\u001b[m\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eun0qdii21WO"
      },
      "source": [
        "### **2.2. Desenvolvimento**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5MiknLIh2460"
      },
      "source": [
        "Gere uma gráfico de linha utilizando os dados do arquivo `gasolina.csv` com o dia no eixo `x`\n",
        " e o seu preço no eixo `y` utilizando os pacotes Python de sua preferência, como o Pandas e o Seaborn. Salve o gráfico no arquivo `gasolina.png` e o seu código Python de geração no arquivo `gasolina.py`."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8B3QgjlpzYdI"
      },
      "source": [
        "> **Nota**: Este gráfico deve alguns elementos diferente do anterior, como título, legenda, etc."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "import pandas as pd\n",
        "import numpy as np"
      ],
      "metadata": {
        "id": "SvJ1Zez6rxi9"
      },
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PPzewPcD3Z8n",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 577
        },
        "outputId": "789d1023-69a1-4cf1-c331-5f539ddb8fa0"
      },
      "source": [
        "df_gasolina\n",
        "plt.figure(figsize=(8,6))\n",
        "plt.xticks(rotation=45)\n",
        "sns.set_theme(style=\"darkgrid\")\n",
        "sns.lineplot(data=df_gasolina, x='dia', y='venda', color='red')"
      ],
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: xlabel='dia', ylabel='venda'>"
            ]
          },
          "metadata": {},
          "execution_count": 45
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 800x600 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAsYAAAIeCAYAAAC4Bcn3AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAB76ElEQVR4nO3dd5hU9d3+8feZOTNb2UYvUsUVkN5UqhQVQbDFEguJoICGJJbkl+ijMcaYxMckRh+jWFA0asSIIBGRKogivUlRpAoIArvsAlumnd8fszuItGV3Zs6U+3VdXGyZci+H3b337Od8v4ZlWRYiIiIiIknOYXcAEREREZFYoGIsIiIiIoKKsYiIiIgIoGIsIiIiIgKoGIuIiIiIACrGIiIiIiKAirGIiIiICKBiLCIiIiICgGl3gERgWRaBgPZJiTSHw9C/cxLScU8+OubJR8c8+UT7mDscBoZhnPF2KsZhEAhYFBQctTtGQjNNB7m5GRQXl+DzBeyOI1Gi4558dMyTj4558rHjmOflZeB0nrkYa5RCRERERAQVYxERERERQMVYRERERARQMRYRERERAVSMRUREREQAFWMREREREUDFWEREREQEUDEWEREREQFUjEVEREREABVjERERERFAxVhEREREBFAxFhEREREBVIxFRERERAAVYxERERERQMVYRERERARQMRYRERERAVSMRUREREQAFWMREREREUDFWERilGPrFrLbnw9//avdUUREJEmoGItITEqdNgXH7l3w5JNgWXbHERGRJKBiLCIxyVy1IvjC3r041621N4yIiCQFFWMRiT2WhWvF8tCrrtkf2RhGRESShYqxiMQcx57dOPZ/F3rdNWe2jWlERCRZqBiLSMwxVwbPFgcaNgLAuWwJRmGBnZFERCQJqBiLSMxxrQzOF3svHwLt2mEEArg/nmdzKhERSXQqxiIScyovvPN16QZXXAGAe67GKUREJLJUjEUktvj9uFavAsDXpeuxYjxvNgQCdiYTEZEEp2IsIjHF+eUmjJKjBDIyCZyXD716YWXWwnHgAOba1XbHExGRBKZiLCIxxVU5RtG5Czid4HLh7X8JAO45s+yMJiIiCU7FWERiirmyshh3Db3NO+hSANxzVYxFRCRyYqoYT5kyhfz8/BP+PPnkk6e8z3fffccTTzzBiBEj6Ny5M3379uW+++5j9+7d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krdbj2AxXraE8h/daHcciWPVKsZXX311uHOITcqGX036P/6Ke+4sjCOHsTJr2R1Jwkwbe8QZw+Do/zxC6muvUHbdDZRfd4MKscgZeLv3gOfBXL7M7igS52q8btN3333Hpk2bKCkpCUceiTL/Be3xtWyFUVaGe9ZMu+NIBJgrlwPg66JiHC/KR1xD0bvTKb/pFpVikSrwVW70seGL4DUzItVU7WI8Z84cLr/8cvr168fVV1/NmjXBXbUKCgq46qqrmD17dthCSgQZBuUjgr8BSNHqFAnHsfdbnHt2YzkceDt0sjuOiEhEBBo2wt/kHIxAANfqlXbHkThWrWI8b948xo8fT25uLnfffTfW95ZHycvLo379+kyZMiVsISWyyocHl21zz5uNceSwzWkknMxVwW8Q/vw2WnVERBJaaNm2ZVrPWKqvWsX42WefpVu3brz11lvcfPPNJ7y/U6dOWpEijvjbtsN3bmuM8nLcH31odxwJo9DGHhqjEJEEFxqnWL7U5iQSz6pVjDdv3syQIUNO+f46depw8ODBaoeSKDMMyodrnCIRuVZUzBfrwjsRSXChHfBWLNNGH1Jt1SrGaWlplJaWnvL933zzDTk5OdXNJDao3AXPPW82xuFim9NIWAQCmBWzdlqRQkQSne+CDlipqTgKCnBu/druOBKnqlWMe/bsydSpU/H5fCe8b//+/UyePJnevXvXOJxEj//8NvjOy8fweHDPnGF3HAkD55avcRwuxkpLw9+mrd1xREQiy+3G17EzAOYyjVNI9VSrGP/iF79g7969XHfddbz99tsYhsGiRYv4+9//zpVXXollWdx9993hziqRZBiUX3kVACnva5wiEYSWaevQCcxqLVkuIhJXQuMUKsZSTdUqxq1ateLNN98kJyeHf/zjH1iWxcsvv8yECRM477zzePPNN2nSpEm4s0qEhcYp5s/FKDpkbxipMVdFMdYYhYgki1Ax1gV4Uk3VOo309ddf07p1a1599VWKiorYsWMHlmVxzjnnkJeXF+6MEiX+89vgyz8f88tNuGfOoPyGH9sdSWqgckUKbewhIsmishg7N23AOFyMVSvL5kQSb6p1xnjYsGFceeWVPP/88xQVFdGhQwc6duyoUpwAQqtTaJwivpWVYa7/AgBvl242hxERiQ6rfn38TZtjWBZmxao8ImejWsX4kUceIS8vj6ef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COvWrbPtQjwVY4kplT9FVn5C+P1+ADIyMigrKwvd7siRI8yfPz/6ASViDMOgadOmpKWlMWvWLADuvfdevvnmG2677TZWrFjB7373O61znCDq1q3L1Vdfzdtvv82//vUvWrVqxQ033MD555/POeecw+9//3uaNWvGjBkztHxfgmjUqBFPP/00999/P8OGDaNBgwb87Gc/o1WrVliWRYMGDXj00UdZvXo169atszuuhFHl9/IePXrQpEkTXnjhBQoLC4FjyzWmpqby05/+lA4dOvD888/b9sORirHEtMqzw7Vq1Qp9Eh0+fJjHH3+ccePGsX//fjvjSRhVfnHs2rUru3bt4v7772fx4sU89dRT3HPPPfz6179myZIllJSU2JxUwuWmm27C6/UyZcoUysrKqFOnDgDl5eXUrVuXe+65h82bN7Nhwwabk0q41K9fn+uvv56LLrqIrVu3hk6COJ1OLMvi4MGD1KlTh9zcXJuTSk2VlJQwffp0IHh8PR4PAI8++ij79+/n17/+NT6fD4fDETp7fM4559CnTx82bNigYixyOm63m9LSUsrKynjiiSeYOXMm//nPf6hbt67d0SRMKr9B9u7dm8mTJ/PJJ5/wt7/9jQsvvJCUlBSuvfZaPvzwQ12QlUCaNWvGY489xoEDB9iwYQMfffQRACkpKQAUFBRQr149ateubWdMiYBatWrRuHFjFixYwL59+4Dg8V60aBENGjRQMY5zpaWl/PjHP+ZXv/oVEydOBILfxwOBAC1btuTBBx9k7dq1jBs3jqKiIgzDCN23RYsWOJ1OSktLbcmui+8kplXOGqelpVFQUMDjjz/O+++/z1tvvRUzax5KeF100UX87W9/Iy8vj+7du4e+YLrdbtxut83pJNzat2/PW2+9xU9/+lMefPBBysvLGTp0KLt372bGjBmkpaWRl5dnd0wJs9TUVB588EFGjRrFjh07qFevHgcOHGDdunVMmjRJxzyO+Xw+nnjiCb777js6d+7MpEmT8Pv93HHHHTgcDhwOB5dccgmWZfH4448zatQoxo8fT6dOnfB6vcybN4+cnBwyMjJsyW9Y359+FolRf//730MX5k2aNIl27drZHUkiqHIpJ0keW7Zs4YknnmDBggU0aNAAt9tNSUkJL774opZpTGBr1qzhH//4BwUFBZx//vnccccdoWW8JD5t27aNcePG0alTJ0aOHMkrr7zC559/zq233sodd9wRup3X6+Wrr77i4YcfZu/evXi9Xpo0acLu3buZNGmSbUtzqhhLXNiwYQOjR4/m9ddf1xdNkQRVWlrK+vXrWb16NfXr16dLly40btzY7lgSYZWzp4B+K5QAysrKmD59OoMHDyYnJ4fNmzfz/PPPs2zZsuPK8fdXn5ozZw7ffPMNWVlZ9OjRI7SXgR1UjCVulJWVkZqaancMEREROY3K3/pVbvO+ZcsW/vnPf55Qjj0eT8z9MKSL7yRuqBSLiIjEvspRuMrtnVu1asVdd91F9+7def3113nppZcA2L9/P2+99RZ79+61LesP6eI7EREREYmoVq1aMW7cOAzD4LXXXqO4uJjt27cza9YsBgwYYHe8EBVjEREREYmoQCDAueeey7hx4ygrK+OFF14gOzubKVOmUL9+fbvjhagYi4iIiEhEVV5ol5WVxdGjR6lVqxZvvPEG5557rs3JjqdiLCIiIiIRV1payp///GcWL17M1KlTY64Ug1alEBEREZEoWbRoEXXr1iU/P9/uKCelYiwiIiIigpZrExEREREBVIxFRERERAAVYxERERERQMVYRERERARQMRYRERERAVSMRUREREQAFWMREREREUDFWEQk6T3zzDPHLbY/YMAAfvOb39iYSETEHirGIiIiIiKAaXcAERGJLTNnzsQwDLtjiIhEnYqxiIgcx+122x1BRMQWGqUQEUkiy5cv59prr6V9+/YMGjSIf//73yfc5oczxocOHeIvf/kLV155JZ07d6ZLly6MHj2aTZs2RTO6iEjE6YyxiEiS+PLLLxk1ahR5eXmMHz8en8/HM888Q+3atU97v2+++YY5c+Zw+eWX06RJEw4cOMDbb7/NLbfcwgcffED9+vWj9BGIiESWirGISJJ4+umnsSyLN954g0aNGgFw2WWXceWVV572fvn5+Xz00Uc4HMd+yThixAiGDBnCf/7zH+6+++6I5hYRiRaNUoiIJAG/38+iRYsYNGhQqBQDtGrVit69e5/2vm63O1SK/X4/hYWFpKen06JFCzZs2BDR3CIi0aQzxiIiSaCgoICysjKaNWt2wvtatGjBggULTnnfQCDAa6+9xptvvsmuXbvw+/2h9+Xk5EQiroiILVSMRUTktJ5//nn+8Y9/cO211/KLX/yC7OxsHA4Hjz/+OJZl2R1PRCRsVIxFRJJAXl4eqamp7Nix44T3bdu27bT3/eijj+jZsyePP/74cW8vLi4mNzc3rDlFROykGWMRkSTgdDrp3bs3c+bMYc+ePaG3b9myhUWLFp3xvj88M/zhhx+yb9++iGQVEbGLzhiLiCSJ8ePH88knn3DzzTdz00034ff7+de//sW5557Ll19+ecr79e/fn2effZbf/va3dO7cma+++orp06dzzjnnRDG9iEjk6YyxiEiSOP/883n55ZfJzc3l6aef5t1332X8+PEMHjz4tPcbO3Yst99+O5988gl//OMfWb9+PRMmTKBhw4ZRSi4iEh2GpSsnRERERER0xlhEREREBFSMRUREREQAFWMREREREUDFWEREREQEUDEWEREREQFUjEVEREREABVjERERERFAxVhEREREBFAxFhEREREBVIxFRERERAAVYxERERERQMVYRERERASA/w8czXrd5dyoxwAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.savefig('gasolina.png')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "b9XVXTycsAUs",
        "outputId": "2a8ed03b-f47c-4dd7-87e2-3e9b9c80ac10"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 0 Axes>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "T51dv46X3YoT"
      },
      "source": [
        "### **2.3. Git**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iyb6rFFX3YoU"
      },
      "source": [
        "Utilizando os comandos do `git`, adicione e \"commite\" os arquivos gerados (base, código Python e gráfico) na branch `develop`."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tRAunRfR4RfG",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e9332eaa-d599-492b-831d-318c514b76c7"
      },
      "source": [
        "# comandos git para adicionar e commitar os arquivos\n",
        "!git add gasolina.csv\n",
        "!git add gasolina.png\n",
        "!git add gasolina.py"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: not a git repository (or any of the parent directories): .git\n",
            "fatal: not a git repository (or any of the parent directories): .git\n",
            "fatal: not a git repository (or any of the parent directories): .git\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git commit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VtyraWozsdIr",
        "outputId": "eaa63ff7-8301-44a9-95a0-842b160cc6e0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: not a git repository (or any of the parent directories): .git\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ozAPHQJu4P00"
      },
      "source": [
        "### **2.4. Github**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2JkFXRdW4P01"
      },
      "source": [
        "Utilizando os comandos do `git`, envie o seu commit para o GitHub."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xEKWMYH75FfC",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "034d4de1-7bfd-4ae5-ccfb-6c0fc7342270"
      },
      "source": [
        "# comandos git para enviar o commit para o GitHub\n",
        "!git commit -m \"arquivo daebacgasolina alterado\""
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fatal: not a git repository (or any of the parent directories): .git\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HX7eUrz90DoF"
      },
      "source": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fM_de4pA0D54"
      },
      "source": [
        "### **2.5. Pull Request e Merge**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "w9byTlNc0D55"
      },
      "source": [
        "No GitHub, crie um *pull request* (PR) para enviar o código da branch de `develop` para a branch `main`. Ainda na plataforma online, confira as atualizações, aprove o PR e realize o *merge*."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "As3enQc2GVm1"
      },
      "source": [
        "---"
      ]
    }
  ]
}